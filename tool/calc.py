import math

# The minimum libs needed
ALLOWED_GLOBALS = {
    "__builtins__": {},
    "math": math
}

# The whole "magic" happens here
def safe_eval(expr: str):
    return eval(expr, ALLOWED_GLOBALS, {})
