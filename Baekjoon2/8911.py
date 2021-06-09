### 거북이
import sys
read = sys.stdin.readline
def solve(l):
    x, y, s = 0, 0, 3 # s방향: 0,1,2,3(동남서북)
    dx, dy = [0], [0]
    for i in l:
        if i == 'F':
            if s == 0: x += 1
            elif s == 1: y -= 1
            elif s == 2: x -= 1
            else: y += 1
        elif i == 'B':
            if s == 0: x -= 1
            elif s == 1: y += 1
            elif s == 2: x += 1
            else: y -= 1
        elif i == 'L':
            s = (s - 1) if s - 1 >= 0 else 3
        elif i == 'R':
            s = (s + 1) if s + 1 <= 3 else 0
        dx.append(x)
        dy.append(y)
    print((max(dx)-min(dx)) * (max(dy)-min(dy)))


dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동, 서, 남, 북
def solve2(l):
    direction = 0
    x, y = (0, 0)
    x_lst, y_lst = [0], [0]
    for i in l:
        if i == 'L':
            direction = (direction + 1) % 4
        elif i == 'R':
            direction = (direction + 3) % 4
        elif i == 'B':
            x -= dx[direction]
            y -= dy[direction] 
        else:
            x += dx[direction]
            y += dy[direction]
        x_lst.append(x)
        y_lst.append(y)
    print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))


tc = int(read())
for _ in range(tc):
    move = list((read().rstrip()))
    # solve(move)
    solve2(move)