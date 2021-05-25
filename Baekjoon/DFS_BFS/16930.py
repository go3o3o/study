### 달리기
from sys import stdin
from collections import deque
n, m, k = map(int, input().split())
gym = [stdin.readline().rstrip() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[-1] * m for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

queue = deque()
queue.append((x1 - 1, y1 - 1))
visited[x1 - 1][y1 - 1] = 0
while queue:
    y, x = queue.popleft()
    if y == x2 - 1 and x == y2 - 1:
        print(visited[y][x])
        break
    for i in range(4):
        for num in range(1, k + 1):
            nx = x + dx[i] * num
            ny = y + dy[i] * num
            if nx < 0 or nx >= m or ny < 0 or ny >= n: break
            if gym[ny][nx] == '#': break
            if visited[ny][nx] == -1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
            elif visited[ny][nx] == visited[y][x] + 1: continue
            else: break