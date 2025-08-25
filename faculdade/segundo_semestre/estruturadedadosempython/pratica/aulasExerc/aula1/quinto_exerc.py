from collections import deque
import time 
n = 20000

lst = list(range(n))
t0 = time.time() 

while lst:
    lst.pop(0)

t1 = time.time()
tempo_list = t1 - t0 

dq = deque(range(n))
t0 = time.time()

while dq:
    dq.popleft()

t1 = time.time()
tempo_deque = t1 - t0 

print(f"Tempo list.pop(0): {tempo_list:.3f} s")
print(f"Tempo deque.popleft: {tempo_deque:.3f} s")
