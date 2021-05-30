### DFS 와 BFS
# n, m, v = map(int, input().split())
# matrix = [[0] * (n + 1) for _ in range(n + 1)]

# for _ in range(m):
#     x, y = list(map(int, input().split()))
#     matrix[x][y] = 1
#     matrix[y][x] = 1

# def bfs(start):
#     visited = [start]
#     queue = [start]
#     while queue:
#         n = queue.pop(0)
#         for c in range(len(matrix[start])):
#             if matrix[n][c] == 1 and (c not in visited):
#                 visited.append(c)
#                 queue.append(c)
#     return visited

# def dfs(start, visited):
#     visited += [start]
#     for c in range(len(matrix[start])):
#         if matrix[start][c] == 1 and (c not in visited):
#             dfs(c, visited)
#     return visited

# print(*dfs(v, []))
# print(*bfs(v))

### DFS와 BFS
def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]
visited = [0 for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

dfs(v)
print()
bfs(v)