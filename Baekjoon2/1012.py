### 유기농 배추
# from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue[0][0], queue[0][1]
        print(x, y)
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] == 1:
                ground[nx][ny] = 0
                queue.append([nx, ny])


tc = int(input())

for _ in range(int(tc)):
    m, n, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]
    result = 0

    for i in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                bfs(i, j)
                ground[i][j] = 0
                result += 1
    
    print(result)
    
