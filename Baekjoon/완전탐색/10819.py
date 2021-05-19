### 차이를 최대로
### 브루트포스

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

def sumOf(exp):
    cnt = 0
    for i in range(len(exp) - 1):
        cnt += abs(exp[i] - exp[(i + 1)])
    return cnt

lst = list(permutations(a, n))

result = []
for i in lst:
    result.append(sumOf(i))

print(result)
print(max(result))