### 로봇 청소기
from collections import deque

def boundary_check(x, y):
    return True if 0 <= x < n and 0 <= y < m else False

def change_direction(d):
    return d - 1 if d != 0 else 3 

def go_back(d):
    return (d + 2) % 4

def cleaning(r, c, d):
    queue = deque([[r, c]])
    room[r][c] = 2
    count = 1 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            d = change_direction(d)
            nx = x + dx[d]
            ny = y + dy[d]

            if boundary_check(nx, ny) and room[nx][ny] == 0:
                queue.append([nx, ny])
                count += 1
                room[nx][ny] = 2
                break
            if i == 3:
                nx, ny = x + dx[go_back(d)], y + dy[go_back(d)]
                queue.append([nx, ny])

                if room[nx][ny] == 1:
                    return count

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
# maze = [stdin.readline().rstrip() for _ in range(n)]

# 북, 동, 남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(cleaning(r, c, d))