# LangChain Basics

This repository demonstrates basic usage of **LangChain** with:

* LLM integration using **Groq**
* **LangSmith tracing** for monitoring and debugging LLM calls
* Configuration management using **Pydantic Settings**
* Execution via **Makefile + uv**

---

## 🔐 Environment Variables Setup

This project relies on environment variables for configuration (API keys, model settings, tracing, etc.).

> These variables are **injected at runtime via Makefile** and consumed using **Pydantic Settings**.

---

### ⚙️ Option 1: Global Setup using (`.bashrc`) (Recommended)

You can define environment variables globally in your local environment.

#### 1. Open your bash configuration:

```bash
nano ~/.bashrc
```

#### 2. Add the following:

```bash
export LLM_GROQ_API_KEY="your_groq_api_key"
export TAVILY_API_KEY="your_tavily_api_key"
export LANGSMITH_API_KEY="your_langsmith_api_key"
export LLM_MODEL="llama-3.1-8b-instant"
export LLM_TEMPERATURE="0.1"
export LANGSMITH_TRACING="true"
export LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
export LANGSMITH_PROJECT="langchain_trace"
```

#### 3. Apply changes:

```bash
source ~/.bashrc
```

#### 4. Verify:

```bash
echo $LLM_GROQ_API_KEY
```

---

### 🚀 Running the Application

The project uses a Makefile to pass environment variables at runtime:

```bash
make run-agent
```

Example (simplified):

```make
run-agent:
	LLM_GROQ_API_KEY=$(LLM_GROQ_API_KEY) \
	TAVILY_API_KEY=$(TAVILY_API_KEY) \
	LANGSMITH_API_KEY=$(LANGSMITH_API_KEY) \
	uv run python -m gen_agent.main
```

---

### 🧠 How It Works

* Environment variables are defined in `.bashrc` (global scope)
* `make run-agent` passes them into the runtime environment
* **Pydantic Settings** reads them inside the application
* No direct dependency on `.env` is required

---

### ⚠️ Notes

* Do **not** hardcode API keys in code
* Do **not** commit secrets to Git
* Rotate keys if exposed
* Restart terminal or run `source ~/.bashrc` if variables are not picked up

---
