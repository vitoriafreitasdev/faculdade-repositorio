import time
from functools import lru_cache

#fibonnaci recursivo
def fib_rec(n: int) -> int:
    #caso base
    if n <= 1:
        return n
    #caso recursivo
    return fib_rec(n - 1) + fib_rec(n - 2)

@lru_cache(maxsize=None)
#fibonnaci com memo
def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


#fibonnaci iterativo
def fib_iter(n: int) -> int: 
    if n <= 1:
        return n
    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

if __name__ == "__main__":
    n = 35
    t0 = time.time()
    print("fib_rec  :", fib_rec(n))
    t1 = time.time()

    print("Tempo de execução: ", t1 - t0)

    t0 = time.time()
    print("fib_memo  :", fib_memo(n))
    t1 = time.time()

    print("Tempo de execução: ", t1 - t0)

    t0 = time.time()
    print("fib_iter  :", fib_iter(n))
    t0 = time.time()

    print("Tempo de execução: ", t1 - t0)



