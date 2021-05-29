### 달이 차오른다, 가자.
import sys 
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, y):
    queue.append([x, y, 0])
    visited[x][y][0] = 1
    while queue:
        x, y, z = queue.popleft()
        if maze[x][y] == '1':
            print(visited[x][y][z] - 1)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] != '#' and visited[nx][ny][z] == 0:
                    if maze[nx][ny].islower():
                        nz = z | (1 << (ord(maze[nx][ny]) - ord('a')))
                        if visited[nx][ny][nz] == 0:
                            visited[nx][ny][nz] = visited[x][y][z] + 1
                            queue.append([nx, ny, nz])
                    elif maze[nx][ny].isupper():
                        if z & (1 << (ord(maze[nx][ny]) - ord('A'))):
                            visited[nx][ny][z] = visited[x][y][z] + 1
                            queue.append([nx, ny, z])
                    else:
                        visited[nx][ny][z] = visited[x][y][z] + 1
                        queue.append([nx, ny, z])
    print(-1)



n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]

visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if maze[i][j] == '0':
            bfs(i, j)