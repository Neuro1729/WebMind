from llm import generate
from search import web_search
from extractor import extract_text

def needs_search(question):
    prompt = f"""
Decide if the question REQUIRES real-time search.
Question: "{question}"
Answer only YES or NO.
"""
    ans = generate(prompt, max_tokens=10)
    return "YES" in ans.upper()

def agent(question):
    # decide route
    if not needs_search(question):
        return generate(f"Answer this question:\n{question}")

    results = web_search(question)

    contexts = []
    for r in results:
        text = extract_text(r["url"])
        if len(text) > 100:
            contexts.append((text, r["url"]))

    # build context block
    ctx = ""
    for i, (text, url) in enumerate(contexts):
        ctx += f"[{i}] {url}\n{text}\n\n"

    prompt = f"""
You are a search assistant. Use ONLY the sources below.

Question: {question}

Sources:
{ctx}

Write a short answer with citations [0], [1], etc.
"""
    return generate(prompt)
