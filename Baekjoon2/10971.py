### 외판원 순회 2
from itertools import combinations
def convert(s):
    s = int(s)
    if s == 0:
        return float('inf')
    return s

n = int(input())
w = [list(map(convert, input().split())) for i in range(n)]
c = {}

def tsp(n, w):
    for k in range(1, n):
        c[(1 + (1<<k), k)] = w[0][k]
    for i in range(2, n + 1):
        for j in combinations(range(1, n), i):
            val = sum(1<<k for k in j) + 1
            for z in j:
                c[(val, z)] = min(c[(val - (1<<z), m)] + w[m][z] for m in j if m != 0 and m != z)
    return min(c[((2 << n -1) - 1, k)] + w[k][0] for k in range(1, n))


print(tsp(n, w))