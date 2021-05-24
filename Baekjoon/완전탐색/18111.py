### 마인크래프트
import sys
n, m, b = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

height = 0
ans = sys.maxsize

dp = [[(i, j) for i in range(n)] for j in range(m)]
print(dp)
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += (i - table[j][k])
            else:
                max += (table[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i
print(ans, height)