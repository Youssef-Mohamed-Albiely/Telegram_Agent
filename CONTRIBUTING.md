# Contributing to Mohamed_Assist

Thanks for your interest in contributing! Here's how to get started.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Telegram-AI-Agent.git`
3. Create a virtual environment and install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your test credentials

## Making Changes

- Create a new branch: `git checkout -b feature/your-feature-name`
- Make your changes
- Test locally with ngrok + a test Telegram bot
- Commit with a clear message: `git commit -m "Add: description of change"`

## Adding a New Tool

1. Open `tools.py`
2. Add your tool using the `@tool` decorator
3. Add it to the `all_tools` list
4. Update the README tools section if it's a significant new capability

## Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR
- Include a short description of what changed and why
- Make sure the server starts without errors before submitting

## Reporting Bugs

Open an issue with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Your Python version and OS
