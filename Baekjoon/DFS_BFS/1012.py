import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


test_case = int(input())

for _ in range(test_case):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        array[y][x] = 1
    result = 0
    for i in range(n): 
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1
    print(result)
