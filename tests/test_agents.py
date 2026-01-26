"""Tests for agent definitions."""

from src.agents import Agent, AGENTS, RESEARCHER, PLANNER, CRITIC


def test_agent_dataclass_fields():
    """Each agent has the required fields."""
    for agent in AGENTS:
        assert isinstance(agent.name, str)
        assert isinstance(agent.role, str)
        assert isinstance(agent.color, str)
        assert isinstance(agent.system_prompt, str)


def test_three_agents_defined():
    """Exactly three agents are registered."""
    assert len(AGENTS) == 3


def test_agent_names():
    """Agents have the expected names."""
    names = [a.name for a in AGENTS]
    assert names == ["Researcher", "Planner", "Critic"]


def test_agents_are_frozen():
    """Agent instances should be immutable."""
    try:
        RESEARCHER.name = "Other"
        assert False, "Should not allow mutation"
    except AttributeError:
        pass


def test_system_prompts_nonempty():
    """Every agent has a non-empty system prompt."""
    for agent in AGENTS:
        assert len(agent.system_prompt) > 0
