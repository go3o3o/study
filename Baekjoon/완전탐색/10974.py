### 모든 순열
from itertools import permutations

def permutations2(selected, k):
    if k == n:
        print(' '.join(list(map(str, selected))))
    else:
        for i in range(1, n + 1):
            if i not in selected:
                permutations2(selected + [i], k + 1)

n = int(input())
permutations2([], 0)

print('----------------------------------------------------')
lst = [i for i in range(1, n +1)]
comb = permutations(lst, n)
for i in comb:
    for j in i:
        print(j, end=' ')
    print()



