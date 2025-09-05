
from functools import lru_cache

def fib_rec(n: int) -> int:

    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_iter(n: int) -> int: 
    if n <= 1:
        return n
    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

if __name__ == "__main__":
    n = 35
    print("fib_rec  :", fib_rec(n))
    print("fib_memo  :", fib_memo(n))
