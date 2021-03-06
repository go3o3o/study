### 2xn 타일링
import sys 
sys.setrecursionlimit(10**6)
n = int(input())

dp = [0] * n
def f_dp(n):
    if n == 1: return 1
    if n == 2: return 2 
    if dp[n - 1]: return dp[n - 1]
    else:
        dp[n - 1] = f_dp(n - 1) + f_dp(n - 2)
        return dp[n-1]

print(f_dp(n) % 10007)