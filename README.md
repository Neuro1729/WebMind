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
