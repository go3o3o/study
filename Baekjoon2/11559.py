### Puyo Puyo
N, M = 12, 6
arr = [[0] * N for _ in range(M)]
for i in range(N):
    tmp = input()
    for j in range(M): arr[j][i] = tmp[j]

dx , dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(X, Y, arr, checked):
    Q = [(X, Y)]
    cnt = 1 
    for (x, y) in Q:
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if 0 <= nx < M and 0 <= nx < N and not checked[nx][ny] and arr[nx][ny] == arr[x][y]:
                checked[nx][ny] = 1 
                cnt += 1
                Q.append((nx, ny))
    if cnt >= 4:
        for (x, y) in Q: arr[x][y] = '.'
        return True
    return False

def step(arr):
    flag = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] != '.':
                checked = [[0] * N for _ in range(M)]
                checked[i][j] = 1
                if bfs(i, j, arr, checked):
                    flag = 1
    if flag:
        for i in range(M):
            new_line = []
            for j in range(N):
                if arr[i][j] != '.':
                    new_line.append(arr[i][j])
            new_line = ['.'] * (N - len(new_line)) + new_line
            arr[i] = new_line
    return flag

ans = 0
for i in range(M * N):
    if step(arr):
        ans += 1
    else:
        break 
print(ans)