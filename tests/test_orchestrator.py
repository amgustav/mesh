"""Tests for orchestrator helpers."""

from src.agents import RESEARCHER, PLANNER
from src.orchestrator import _build_messages


def test_build_messages_empty_history():
    """First agent with no history gets the intro prompt."""
    msgs = _build_messages("do something", [], RESEARCHER)
    assert len(msgs) == 1
    assert msgs[0]["role"] == "user"
    assert "TASK: do something" in msgs[0]["content"]
    assert "first to respond" in msgs[0]["content"]


def test_build_messages_with_history():
    """Agent with prior history sees the conversation."""
    history = [{"agent": "Researcher", "content": "Here are facts."}]
    msgs = _build_messages("do something", history, PLANNER)
    assert len(msgs) == 1
    content = msgs[0]["content"]
    assert "Conversation so far" in content
    assert "Here are facts." in content
    assert "do not repeat" in content.lower()


def test_build_messages_contains_task():
    """The task string always appears in the prompt."""
    task = "plan a trip to Mars"
    msgs = _build_messages(task, [], RESEARCHER)
    assert task in msgs[0]["content"]
