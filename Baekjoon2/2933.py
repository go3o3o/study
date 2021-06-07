### 미네랄
def crush(h, d):
    rr = R - h
    cc = pos[d]
    dc = dy[d]

    while rr >= 0 and rr < R and cc >= 0 and cc < C:
        if cave[rr][cc] == 'x':
            cave[rr][cc] = '.'
            break

        cc += dc

def check():
    for r in range(R):
        for c in range(C):
            visited[r][c] = False
    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x':
                if visited[r][c]:
                    continue
                bfs(r, c)

def bfs(r, c):
    queue = [[r, c]]
    group = [[r, c]]
    flag = False
    while queue:
        _queue = []
        for x, y in queue:
            if x == R-1:
                flag = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and cave[nx][ny] == 'x':
                    _queue.append([nx, ny])
                    visited[nx][ny] = True

        queue = _queue
        group += _queue

    if not flag:
        down(group)


def down(group):
    flag = True
    for r, c in group:
        cave[r][c] = '.'
    while flag:
        for r, c in group:
            if r + 1 < R:
                if cave[r+1][c] == 'x':
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            for i in range(len(group)):
                group[i][0] += 1
    for r, c in group:
        cave[r][c] = 'x'
        visited[r][c] = True


R, C = list(map(int, input().split()))
cave = [list(input()) for _ in range(R)]

n = int(input())
arr = list(map(int, input().split()))
visited = [[False] * C for _ in range(R)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
pos = [0, C-1]

for i in range(len(arr)):
    crush(arr[i], i%2)
    check()

for m in cave:
    print(''.join(m))