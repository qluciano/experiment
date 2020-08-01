

def fib(n):
    x, y = 1, 1
    for _ in range(n - 1):
        x, y = y, x + y
    return y
