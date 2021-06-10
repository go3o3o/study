### 차이를 최대로
from itertools import permutations
n = int(input())
a = list(map(int, input().split()))

def cal(c):
    cnt = 0
    for i in range(len(c) - 1):
        cnt += abs(c[i] - c[i+1])
    return cnt

lst = permutations(a, n)
result = []
for i in lst:
    result.append(cal(i))

print(max(result))