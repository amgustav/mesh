# mesh

3 AI agents arguing about your problems.

![demo](demo.gif)

## What is this?

I wanted to see what happens when you give three AI agents different jobs and let them talk to each other. Turns out they actually catch each other's mistakes and build on each other's ideas. It's fun to watch.

You type a question, and a Researcher, Planner, and Critic go back and forth for a couple rounds in your terminal. Then you get a final answer that's better than what any single agent would've come up with.

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
python3 -m src.mesh "design a morning routine for productivity"
```

## How it works

1. You give it a task
2. Three agents take turns over 2 rounds:
   - **Researcher** (cyan) — digs up relevant info
   - **Planner** (green) — structures everything
   - **Critic** (yellow) — pokes holes, suggests fixes
3. Each agent sees the full conversation so far
4. You get a final combined answer at the end

## Requirements

- Python 3.11+
- Anthropic API key
