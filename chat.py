from model.ollama import ask_llm
from pathlib import Path
from tool.calc import safe_eval

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

while True:
    q = input("> ")
    if q.lower() in {"exit", "quit"}:
        break

    calc_prompt = Path("prompt/calc.txt").read_text()

    decision = route(q)

    if "KB" in decision:
        print(answer_with_kb(q))
    elif "CALC" in decision:
        expr = ask_llm(calc_prompt.format(question=q)).strip()
        result = safe_eval(expr)
        print(result)
