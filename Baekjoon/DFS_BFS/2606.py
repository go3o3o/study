from collections import deque

def dfs(v):
    visited.append(v)
    for e in graph[v]:
        if not e in visited:
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not v in visited:
            visited.append(v)
        for e in graph[v]:
            if not e in visited:
                q.append(e)

c = int(input())
pair = int(input())
graph = [[] for _ in range(c + 1)]

for _ in range(pair):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
visited = []
dfs(1)
print(len(visited) - 1)

visited = []
bfs(1)
print(len(visited) - 1)