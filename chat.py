from model.ollama import ask_llm
from pathlib import Path

router_prompt = Path("prompt/prompt.txt").read_text()
kb = Path("kb/kb.md").read_text()

def route(question):
    prompt = router_prompt.format(question=question)
    return ask_llm(prompt).strip()

def answer_with_kb(question):
    prompt = f"""
Use ONLY the knowledge below.

Knowledge:
{kb}

Question:
{question}
"""
    return ask_llm(prompt)

def call_tool(question):
    return "Tool called (fake response)"

while True:
    q = input("> ")
    if q.lower() in {"exit", "quit"}:
        break

    decision = route(q)

    if "KB" in decision:
        print(answer_with_kb(q))
    else:
        print(call_tool(q))
