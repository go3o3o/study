### 로또
### combinations 함수 이용
"""
from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    s = list(combinations(s, 6))
    for i in s:
        for j in i:
            print(j, end=' ')
        print()
    print()
"""
### dfs 이용
def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)

combi = [0 for i in range(13)]
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()
