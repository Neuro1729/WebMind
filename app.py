from fastapi import FastAPI, Query
from agent import agent  # import your existing agent function

app = FastAPI(title="WebMind API", description="Mini Perplexity-style Search Agent", version="1.0")

@app.get("/ask")
def ask(q: str = Query(..., description="Question to ask the AI agent")):
    """
    Ask any question to the WebMind agent.
    Example: /ask?q=who+is+elon+musk
    """
    answer = agent(q)
    return {"question": q, "answer": answer}
