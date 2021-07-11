n, m, v = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y) 
    matrix[y].append(x)
print(matrix.sort)
for i in range(len(matrix)):
    matrix[i].sort()
print(matrix)
def bfs(v):
    queue = [v]
    visited[v] = 1
    result.append(v)
    while queue:
        q = queue.pop(0)
        for i in matrix[q]:
            if visited[i] == 0:
                result.append(i)
                queue.append(i)
                visited[i] = 1

def dfs(v):
    visited[v] = 1
    result.append(v)
    for i in matrix[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


result = []
visited = [0] * (n + 1)
dfs(v)
print(*result)

result = []
visited = [0] * (n + 1)
bfs(v)
print(*result)
