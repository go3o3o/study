### DFS 와 BFS
n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    matrix[x][y] = 1
    matrix[y][x] = 1 

def bfs(v):
    queue = [v]
    visited = [v]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[v])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

def dfs(v, visited):
    visited += [v]
    for c in range(len(matrix[v])):
        if matrix[v][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited

print(*dfs(v, []))
print(*bfs(v))
