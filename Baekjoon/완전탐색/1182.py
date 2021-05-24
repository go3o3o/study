### 부분수열의 합 
from itertools import combinations
n, s = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for i in range(1, n + 1):
    sub = list(combinations(lst, i))
    for c in sub:
        if sum(c) == s:
            result += 1
print(result)

result = 0
def dfs(idx, sum):
    global result
    if idx >= n:
        return
    sum += lst[idx]
    if sum == s:
        result += 1
    dfs(idx + 1, sum - lst[idx])
    dfs(idx + 1, sum)
dfs(0, 0)
print(result)