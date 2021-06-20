from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        # print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visitied[nx][ny] == 1:
                visitied[nx][ny] = 0
                queue.append((nx, ny))
        

tc = int(input())

for _ in range(tc):
    m, n, k = map(int, input().split())
    visitied = [[0] * m for _ in range(n)] 
    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        visitied[y][x] = 1 
    for i in range(n):
        for j in range(m):
            if visitied[i][j] == 1:
                bfs(i, j)
                visitied[i][j] = 0
                result += 1
    print(result)