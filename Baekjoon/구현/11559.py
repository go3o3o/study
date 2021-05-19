### Puyo Puyo
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
graph = []
result = 0

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b))

    pang = deque()
    pang.append((a, b))

    visited = [[False] * 6 for _ in range(12)]
    visited[a][b] = True
    count = 1
    flag = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == c and not visited[nx][ny]:
                queue.append((nx, ny))
                pang.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    if count >= 4:
        flag = 1
        for x, y in pang:
            graph[x][y] = '.'

    return flag


def gravity():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1):
            if graph[x][y] != '.':
                queue.append(graph[x][y])
        for x in range(11, -1, -1):
            if queue:
                graph[x][y] = queue.popleft()
            else:
                graph[x][y] = '.'

for i in range(12):
    graph.append(list(input()))

while True:
    chk = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                chk += bfs(i, j, graph[i][j])
            
    if chk == 0:
        print(result)
        break
    else:
        result += 1
    gravity()