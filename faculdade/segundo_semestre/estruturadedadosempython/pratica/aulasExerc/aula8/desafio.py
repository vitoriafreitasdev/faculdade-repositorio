# problema da soma de subconjunto

def subconjunto(nums, S, n=None):
    if n is None:
        n = len(nums)
    if S == 0:
        return True
    if n == 0:
        return False
    if nums[n-1] > S:
        return subconjunto(nums, S, n-1)
    return subconjunto(nums, S, n-1) or subconjunto(nums, S - nums[n-1], n-1)

def subconjunto_memo(nums, S):
    memo = {}
    def dp(n, s):
        if s == 0:
            return True
        if n == 0:
            return False
        if (n, s) in memo:
            return memo[(n, s)]
        if nums[n-1] > s:
            memo[(n, s)] = dp(n-1, s)
        else:
            memo[(n, s)] = dp(n-1, s) or dp(n-1, s - nums[n-1])
        return memo[(n, s)]
    return dp(len(nums), S)

def subconjunto_bottom(nums, S):
    n = len(nums)
    dp = [[False]*(S+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for s in range(1, S+1):
            if nums[i-1] > s:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
    return dp[n][S]

# problema do troco mínimo

def troco_minimo(coins, V):
    if V == 0:
        return 0
    res = float('inf')
    for c in coins:
        if c <= V:
            res = min(res, 1 + troco_minimo(coins, V - c))
    return res


def troco_minimo_memo(coins, V):
    memo = {}
    def dp(v):
        if v == 0:
            return 0
        if v in memo:
            return memo[v]
        res = float('inf')
        for c in coins:
            if c <= v:
                res = min(res, 1 + dp(v - c))
        memo[v] = res
        return res
    return dp(V)


import time

nums = [3, 34, 4, 12, 5, 2]
S_values = [9, 15, 30]  
coins = [1, 2, 5, 10, 25]
V_values = [11, 27, 63] 


for S in S_values:
    t1 = time.time()
    subconjunto(nums, S)
    t2 = time.time()
    subconjunto_memo(nums, S)
    t3 = time.time()
    subconjunto_bottom(nums, S)
    t4 = time.time()
    print(f"S = {S}")
    print(f"Recursiva: {t2-t1:.6f}s, Memoização: {t3-t2:.6f}s, Bottom-up: {t4-t3:.6f}s")
