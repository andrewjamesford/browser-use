
# Agent Ollama R1 & Claude 3.5 sonnet & gpt-4o browser-use demo

This demo app shows how you can use 3 different LLM models to perform browser navigation and return the search results of comparing API prices.

## Getting started

Clone the repo, then install `uv` the python dependency and everything else tool (if you haven't already).

Create a .env file with the following variables and appropriate keys.

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

## Installation

Install via uv venv

```sh
uv venv --python 3.11
```

Activate it
```sh
# For Mac/Linux:
source .venv/bin/activate

# For Windows:
.venv\Scripts\activate

```

Install dependencies
```sh
uv pip install browser-use
playwright install
```

## Running agents

To run the agent make sure you have the appropriate keys in an `.env` file. If using Ollama install the ollama application and pull the appropriate model you wish to use.

For example:

```sh
python ./agent-claude35-sonnet.py
```

The call will return a JSON response and generate a gif file. To do this it will use playwright to open a chromium browser and perform navigation of websites to get the appropriate information.

