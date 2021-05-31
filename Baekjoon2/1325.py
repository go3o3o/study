### 효율적인 해킹
from collections import deque

n, m = map(int, input().split())
matrix = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[b].append(a)

def dfs(v):
    visited[v] = True
    count = 1
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

def bfs(v):
    queue = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    count = 1
    while queue:
        v = queue.popleft()
        for e in matrix[v]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                count += 1

    return count 

result = []
max_value = -1 

for i in range(1, n + 1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
print(*result)

visited = [False] * (n + 1)
result = []
max_value = -1
for i in range(1, n + 1):
    c = dfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
print(*result)