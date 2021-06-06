### 바이러스
from collections import deque
n = int(input())
c = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(c):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if not v in visited:
            visited.append(v)
        for i in graph[v]:
            if not i in visited:
                queue.append(i)
visited = []
bfs(1)
# print(graph)
print(len(visited) - 1)
