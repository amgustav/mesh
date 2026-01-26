"""Orchestrator — coordinates agent communication and turn-taking."""

import re

import anthropic
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .agents import Agent, AGENTS
from .config import ANTHROPIC_API_KEY, MODEL, MAX_TOKENS, SYNTHESIS_MAX_TOKENS


console = Console()


def _strip_markdown_bold(text: str) -> str:
    """Remove **bold** markers from text for clean terminal output."""
    return re.sub(r"\*\*(.+?)\*\*", r"\1", text)


def _build_messages(
    task: str,
    history: list[dict[str, str]],
    agent: Agent,
) -> list[dict[str, object]]:
    """Build the message list for an agent's API call."""
    messages: list[dict[str, object]] = []

    # First message: the task and any conversation so far
    conversation_text = f"TASK: {task}\n"
    if history:
        conversation_text += "\n--- Conversation so far ---\n"
        for entry in history:
            conversation_text += f"\n[{entry['agent']}]: {entry['content']}\n"
        conversation_text += "\n--- End of conversation ---\n"
        conversation_text += (
            f"\nYou are {agent.name}. Respond with your contribution. "
            "Build on what others have said — do not repeat."
        )
    else:
        conversation_text += (
            f"\nYou are {agent.name}. You are the first to respond. "
            "Provide your initial contribution to this task."
        )

    messages.append({"role": "user", "content": conversation_text})
    return messages


def _call_agent(
    client: anthropic.Anthropic,
    agent: Agent,
    task: str,
    history: list[dict[str, str]],
) -> str:
    """Call a single agent and return its response text."""
    messages = _build_messages(task, history, agent)

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=agent.system_prompt,
        messages=messages,
    )

    return _strip_markdown_bold(response.content[0].text)


def _generate_final_output(
    client: anthropic.Anthropic,
    task: str,
    history: list[dict[str, str]],
) -> str:
    """Generate a final consolidated output from the full conversation."""
    conversation_text = ""
    for entry in history:
        conversation_text += f"[{entry['agent']}]: {entry['content']}\n\n"

    messages = [
        {
            "role": "user",
            "content": (
                f"TASK: {task}\n\n"
                f"Here is the full multi-agent conversation:\n\n{conversation_text}\n"
                "Synthesize everything above into a single, polished final output "
                "that directly addresses the original task. Combine the best elements "
                "from all agents. Be comprehensive but concise. Do not mention the "
                "agents or the conversation — just deliver the final result."
            ),
        }
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=SYNTHESIS_MAX_TOKENS,
        system="You produce clear, well-structured final outputs by synthesizing multi-agent discussions. Use plain text only, no markdown. Use - for bullet points. Keep your response brief and complete all sentences.",
        messages=messages,
    )

    return _strip_markdown_bold(response.content[0].text)


def run(task: str) -> str:
    """Run the multi-agent orchestration loop and return the final output."""
    if not ANTHROPIC_API_KEY:
        console.print(
            "[bold red]Error:[/] ANTHROPIC_API_KEY not set. "
            "Copy .env.example to .env and add your key."
        )
        raise SystemExit(1)

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    history: list[dict[str, str]] = []

    console.print()
    console.print(
        Panel(
            Text(task, style="bold white"),
            title="[bold]Task",
            border_style="bright_blue",
        )
    )
    console.print()

    for current_round in range(1, 2):
        console.rule(f"[dim]Round {current_round}[/dim]", style="dim")
        console.print()

        for agent in AGENTS:
            # Show thinking indicator
            with console.status(
                f"[{agent.color}]{agent.name} is thinking...[/{agent.color}]",
                spinner="dots",
            ):
                try:
                    response_text = _call_agent(client, agent, task, history)
                except anthropic.APIError as e:
                    console.print(f"[bold red]API error for {agent.name}:[/] {e}")
                    continue

            # Display agent response
            console.print(
                Text(f"[{agent.name}]", style=f"bold {agent.color}"),
                end=" ",
            )
            console.print(response_text)
            console.print()

            history.append({"agent": agent.name, "content": response_text})

    # Generate final output
    console.print()
    with console.status("[bold white]Generating final output...[/]", spinner="dots"):
        final = _generate_final_output(client, task, history)

    console.print()
    console.print(
        Panel(
            final,
            title="[bold]Final Output[/bold]",
            border_style="bright_white",
            padding=(1, 2),
        )
    )
    console.print()

    return final
