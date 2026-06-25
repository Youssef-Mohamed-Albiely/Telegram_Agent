# 🤖 Mohamed_Assist — Telegram AI Agent

A production-ready conversational AI Agent for Telegram, built with **FastAPI**, **LangChain**, and **Groq LPU** for blazing-fast inference. Features per-user session management, summarization-based long-term memory, and agentic tool-use.

---

## ✨ Features

- **Conversational AI** — powered by Groq's LPU inference engine (ultra-low latency)
- **Per-user Session Management** — each Telegram user gets their own isolated conversation context
- **Smart Memory** — sliding window + automatic summarization to preserve context without hitting token limits
- **Tool-use Agent** — extensible tool system (SerpAPI web search, current date, and more)
- **FastAPI Webhook Server** — async, production-grade endpoint for Telegram's webhook API
- **LangSmith Observability** — full tracing and monitoring of every agent run
- **Anti-prompt-injection** — system-level guardrails against user manipulation attempts

---

## 🏗️ Architecture

```
Telegram User
     │
     ▼
POST /webhook  (FastAPI)
     │
     ▼
pipeline_with_history  (RunnableWithMessageHistory)
     │
     ├── System Prompt (identity, rules, safety)
     ├── Chat History  (per user_id, summary memory)
     ├── User Input
     └── Agent Scratchpad
     │
     ▼
AgentExecutor  (LangChain)
     │
     ├── LLM: Groq (llama-3.3-70b-versatile)
     └── Tools: SerpAPI · current_date · [extensible]
     │
     ▼
send_message()  →  Telegram Bot API
```

---

## 🗂️ Project Structure

```
Telegram_Bot/
├── main.py                  # FastAPI app, webhook endpoint, Telegram send
├── agent_ex.py              # Agent, prompt template, session factory
├── memory.py                # Custom summarization memory (BaseChatMessageHistory)
├── tools.py                 # Custom LangChain tools
├── initialize_llm.py        # LLM initialization (Groq via OpenAI-compatible API)
├── Initialize_LangSmith.py  # LangSmith tracing setup
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
└── .gitignore
```

---

## ⚡ Quick Start

### 1. Clone & install

```bash
git clone https://github.com/Youssef-Mohamed-Albiely/Telegram-AI-Agent.git
cd Telegram-AI-Agent
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# Fill in your keys inside .env
```

| Variable | Description | Where to get it |
|---|---|---|
| `ACCESS_TOKEN` | Telegram Bot Token | [@BotFather](https://t.me/BotFather) on Telegram |
| `GROQ_API_KEY` | Groq LPU API key | [console.groq.com](https://console.groq.com) |
| `SERPAPI_API_KEY` | Web search API key | [serpapi.com](https://serpapi.com) |
| `LANGCHAIN_API_KEY` | LangSmith tracing (optional) | [smith.langchain.com](https://smith.langchain.com) |

### 3. Run the server

```bash
uvicorn main:app --reload --port 8000
```

### 4. Expose locally with ngrok (for development)

```bash
ngrok http 8000
```

### 5. Set Telegram Webhook

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://<your-ngrok-url>/telegram-webhook"}'
```

---

## 🧠 Memory System

The agent uses a **custom summarization memory** (`memory.py`):

- Keeps the last `k` messages (default: 20) in the context window
- When messages exceed `k`, older ones are **automatically summarized** by the LLM and stored as a `SystemMessage`
- The summary is prepended to the chat history on every new turn
- Each user gets their own isolated `memory` instance, keyed by Telegram `user_id`

---

## 🛠️ Adding New Tools

Create a new tool in `tools.py`:

```python
from langchain.tools import tool

@tool
def my_new_tool(query: str) -> str:
    """Describe what this tool does. The agent reads this docstring."""
    # your logic here
    return result

all_tools = [current_date, my_new_tool]
```

Tools are automatically picked up by the agent in `agent_ex.py`.

---

## 🚀 Deployment

### Environment variables on your server

Make sure all variables from `.env.example` are set in your deployment environment (Railway, Render, VPS, etc.).

### Set production webhook

After deploying, update your Telegram webhook to your production URL:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://your-production-domain.com/telegram-webhook"}'
```

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| Web Framework | FastAPI + Uvicorn |
| AI Framework | LangChain |
| LLM Provider | Groq (llama-3.3-70b-versatile) |
| Memory | Custom summarization (LangChain BaseChatMessageHistory) |
| Web Search | SerpAPI |
| Observability | LangSmith |
| Messaging | Telegram Bot API |

---

## 🔒 Security Notes

- **Never commit your `.env` file** — it's excluded by `.gitignore`
- The `.env.example` file is safe to commit — it contains no real secrets
- For production, consider adding webhook secret token verification (Telegram supports `secret_token` in `setWebhook`)

---

## 👨‍💻 Author

**Mohamed Ali El-Biely** — AI Agent Developer  
GitHub: [@Youssef-Mohamed-Albiely](https://github.com/Youssef-Mohamed-Albiely)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
