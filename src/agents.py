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
    system_prompt="Gather key facts briefly. Under 50 words.",
)

PLANNER = Agent(
    name="Planner",
    role="organizer and structurer",
    color="green",
    system_prompt="Turn facts into actionable steps. Under 50 words.",
)

CRITIC = Agent(
    name="Critic",
    role="reviewer and improver",
    color="yellow",
    system_prompt="Spot gaps and suggest fixes. Under 50 words.",
)

AGENTS: list[Agent] = [RESEARCHER, PLANNER, CRITIC]
