def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if a < b:
        raise ValueError(f"{b} cannot be greater than {a}")
    return a // b
