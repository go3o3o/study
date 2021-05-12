### DFS와 BFS
from collections import deque

def dfs(v):
    visited.append(v)
    # print(graph[v])
    for e in graph[v]:
        # print(e)
        if not e in visited:
            dfs(e)

def bfs(v):
    visited.append(v)
    q = deque([v])
    while q:
        v = q.popleft()
        if not v in visited:
            visited.append(v)
        for e in graph[v]:
            if not e in visited:
                q.append(e)
    pass

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
for e in graph: 
    e.sort()
# visited = [False] * (n + 1)
visited = []
dfs(v)
print(visited)

visited = []
bfs(v)
print(visited)
