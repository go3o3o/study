### 외판원 순회 2

import sys

def dfs(start, next, value, visited):
    global min_val
    if len(visited) == n:
        if travel[next][start] != 0:
            min_val = min(min_val, value + travel[next][start])
        return
    for i in range(n):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()

n = int(input())

travel = [list(map(int, input().split())) for _ in range(n)]
min_val = sys.maxsize

for i in range(n):
    dfs(i, i, 0, [i])

print(min_val)