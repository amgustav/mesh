"""Agent definitions for mesh — name, role, system prompt, and color."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Agent:
    """An AI agent with a specific role in the collaboration."""

    name: str
    role: str
    color: str
    system_prompt: str


RESEARCHER = Agent(
    name="Researcher",
    role="information gatherer",
    color="cyan",
    system_prompt=(
        "Researcher agent. Gather key facts and data for the task. "
        "Be concise. Don't repeat others. Under 100 words."
    ),
)

PLANNER = Agent(
    name="Planner",
    role="organizer and structurer",
    color="green",
    system_prompt=(
        "Planner agent. Organize information into actionable steps. "
        "Build on others' input. Be specific. Under 100 words."
    ),
)

CRITIC = Agent(
    name="Critic",
    role="reviewer and improver",
    color="yellow",
    system_prompt=(
        "Critic agent. Identify gaps and suggest fixes. "
        "Be constructive and specific. Under 100 words."
    ),
)

AGENTS: list[Agent] = [RESEARCHER, PLANNER, CRITIC]
