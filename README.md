# mesh

Agents collaborating in your terminal.

![demo](demo.gif)

## What is this?

I wanted to see what happens when you give three AI agents different jobs and let them talk to each other. You give it a task, a Researcher, Planner, and Critic discuss it for a couple rounds in your terminal, and you get the output.

## Install

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your Anthropic API key to .env
```

## Usage

```bash
python3 -m src.mesh "plan a weekend trip to Tokyo"
python3 -m src.mesh "compare React vs Svelte for a small project"
python3 -m src.mesh "design a productive morning routine"
```

## How it works

1. You give it a task
2. Three agents take turns over 2 rounds:
   - **Researcher** (cyan) — finds info
   - **Planner** (green) — organizes it
   - **Critic** (yellow) — finds what's missing
3. Each agent sees the full conversation so far
4. Then you get one final answer

## Requirements

- Python 3.11+
- Anthropic API key
