### 행렬 곱셈 순서
import sys

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for i in range(n)]
for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = sys.maxsize
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])

print(dp[0][n - 1])
