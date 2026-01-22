import math

ALLOWED_GLOBALS = {
    "__builtins__": {},
    "math": math
}

def safe_eval(expr: str):
    return eval(expr, ALLOWED_GLOBALS, {})
