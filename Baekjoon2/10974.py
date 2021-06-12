### 모든 순열
from itertools import permutations

n = int(input())
lst = [i for i in range(1, n + 1)]
# print(n^2)
comb = permutations(lst, n)
for i in comb:
    print(' '.join(list(map(str, i))))
   