### 부분수열의 합
from itertools import combinations

n, s = map(int, input().split())
lst = list(map(int, input().split()))

result = 0 
for i in range(1, n + 1):
    sub = list(combinations(lst, i))
    for j in sub:
        if sum(j) == s:
            result += 1
print(result)