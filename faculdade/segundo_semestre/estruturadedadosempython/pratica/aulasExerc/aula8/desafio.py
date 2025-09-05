def subconjunto(numeros, S, n=None):
    if n is None:
        n = len(numeros)
    if S == 0:
        return True
    if n == 0:
        return False
    if numeros[n-1] > S:
        return subconjunto(numeros, S, n-1)
    return subconjunto(numeros, S, n-1) or subconjunto(numeros, S - numeros[n-1], n-1)

def subconjunto_memo(numeros, S):
    memo = {}
    def dp(n, s):
        if s == 0:
            return True
        if n == 0:
            return False
        if (n, s) in memo:
            return memo[(n, s)]
        if numeros[n-1] > s:
            memo[(n, s)] = dp(n-1, s)
        else:
            memo[(n, s)] = dp(n-1, s) or dp(n-1, s - numeros[n-1])
        return memo[(n, s)]
    return dp(len(numeros), S)

def subconjunto_bottom(numeros, S):
    n = len(numeros)
    dp = [[False]*(S+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for s in range(1, S+1):
            if numeros[i-1] > s:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - numeros[i-1]]
    return dp[n][S]

# Problema do troco mínimo 

def troco_minimo(coins, V):
    if V == 0:
        return 0
    if V < 0:
        return float('inf')  
    resposta = float('inf')
    for c in coins:
        if c <= V:
            sub_resposta = troco_minimo(coins, V - c)
            if sub_resposta != float('inf'):
                resposta = min(resposta, 1 + sub_resposta)
    return resposta

def troco_minimo_memo(moedas, V):
    memo = {}
    def dp(v):
        if v == 0:
            return 0
        if v < 0:
            return float('inf')
        if v in memo:
            return memo[v]
        resposta = float('inf')
        for m in moedas:
            if m <= v:
                sub_resposta = dp(v - m)
                if sub_resposta != float('inf'):
                    resposta = min(resposta, 1 + sub_resposta)
        memo[v] = resposta
        return resposta
    return dp(V)

def troco_minimo_bottom(moedas, V):
 
    dp = [float('inf')] * (V + 1)
    dp[0] = 0
    
    for v in range(1, V + 1):
        for m in moedas:
            if m <= v:
                dp[v] = min(dp[v], 1 + dp[v - m])
    
    return dp[V] if dp[V] != float('inf') else -1 

import time

numeros = [3, 34, 4, 12, 5, 2]
Svalores = [9, 15, 30]  
moedas = [1, 2, 5, 10, 25]
Vvalores = [11, 27, 63] 

print("PROBLEMA DO SUBCONJUNTO")
for S in Svalores:
    t1 = time.time()
    resultado1 = subconjunto(numeros, S)
    t2 = time.time()
    resultado2 = subconjunto_memo(numeros, S)
    t3 = time.time()
    resultado3 = subconjunto_bottom(numeros, S)
    t4 = time.time()
    
    print(f"S = {S}")
    print(f"Resultados: Rec={resultado1}, Memo={resultado2}, Bottom={resultado3}")
    print(f"Tempos: Recursiva: {t2-t1:.6f}s, Memoização: {t3-t2:.6f}s, Bottom-up: {t4-t3:.6f}s")
    print()

print("\nPROBLEMA DO TROCO MÍNIMO")
for V in Vvalores:
    t1 = time.time()
    resultado1 = troco_minimo(moedas, V)
    t2 = time.time()
    resultado2 = troco_minimo_memo(moedas, V)
    t3 = time.time()
    resultado3 = troco_minimo_bottom(moedas, V)
    t4 = time.time()
    
    print(f"V = {V}")
    print(f"Resultados: Rec={resultado1}, Memo={resultado2}, Bottom={resultado3}")
    print(f"Tempos: Recursiva: {t2-t1:.6f}s, Memoização: {t3-t2:.6f}s, Bottom-up: {t4-t3:.6f}s")
    print()