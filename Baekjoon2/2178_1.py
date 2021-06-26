from collections import deque

n, m = map(int, input().split())
maze = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
queue = [(0, 0)]
visited[0][0] = 1

def bfs():
    while queue:
        x, y = queue.pop(0)

        if x == n-1 and y == m-1:
            print(visited[x][y])
            break 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 1 and maze[nx][ny] == '1':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))