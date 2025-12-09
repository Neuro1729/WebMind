# 🚀 WebMind

A mini Perplexity-style agent that searches the web and answers with sources.

---

## ✨ Features

A small AI agent that:

* **Detects** if a user question needs a web search.
* **Calls** the **Tavily Search API**.
* **Fetches** top webpages using `requests` + **Newspaper3k** / **BeautifulSoup**.
* **Extracts** clean text from the pages.
* **Summarizes** and **answers** using **Qwen 2.5B** / **Llama 3 3B**.
* **Returns** a clean final answer with citations.

---

## 💻 Installation

To get the project running on your local machine, install the required Python libraries using the following command:

```bash
pip install fastapi uvicorn tavily-python newspaper3k beautifulsoup4 requests langchain qwen-vl-utils transformers accelerate
```

---

## 🔑 Configuration: Set API Key

Before running the agent, you must set your Tavily API Key as an environment variable.

- macOS / Linux (bash, zsh):

    ```bash
    export TAVILY_API_KEY="your_api_key_here"
    ```

- Windows (PowerShell):

    ```bash
    setx TAVILY_API_KEY "your_api_key_here"
    ```
## ▶️ Run the Agent From CLI

Ask any question directly from the terminal:

```bash
python cli.py "what is the higgs boson"
```


## ▶️ Run the FastAPI Server

To start the WebMind API server, run the following command in your terminal:

```bash
uvicorn app:app --reload

