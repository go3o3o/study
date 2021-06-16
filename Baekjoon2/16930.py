### 달리기
import sys 
from collections import deque 

# n, m, k = map(int, input().split())
# grid = [input() for _ in range(n)]
# x1, y1, x2, y2 = map(int, input().split())

# visited = [[-1] * m for _ in range(n)]
# visited[x1 - 1][y1 - 1] = 0 
# dx, dy = [-1, 1, 0, 1], [0, 0, -1, 1]

# queue = deque()
# queue.append((x1 - 1, y1 - 1))

# while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#         for j in range(1, k+1):
#             nx, ny = x + j * dx[i], y + j * dy[i]
#             if not 0 <= nx < n and 0 <= ny < m or grid[nx][ny] == '#': break
#             if visited[nx][ny] <= visited[x][y] != -1: break
#             if visited[nx][ny] != -1: continue
#             visited[nx][ny] = visited[x][y] + 1
#             queue.append((nx, ny))
# print(visited[x2 - 1][y2 - 1])

di = (-1,1,0,0)
dj = (0,0,-1,1)

n, m, limit = map(int, input().split())
grid = [input().strip() for i in range(n)]
i1, j1, i2, j2 = map(int,input().split())
vis = [[-1]*m for i in range(n)]; vis[i1-1][j1-1] = 0
Q = deque([(i1-1, j1-1)])
while Q:
    i, j = Q.popleft()
    for d in range(4):
        for k in range(1, limit+1):
            ni, nj = i+k*di[d], j+k*dj[d]
            if not (0<=ni<n and 0<=nj<m) or grid[ni][nj] == '#': break
            if -1 != vis[ni][nj] <= vis[i][j]: break
            if -1 != vis[ni][nj]: continue
            vis[ni][nj] = vis[i][j]+1; Q.append((ni,nj))
print(vis[i2-1][j2-1])