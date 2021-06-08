### 거북이

tc = int(input())
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # 동, 서, 남, 북

def dfs(x, y):
    print(x, y)

for _ in range(tc):
    direction = list(map(str, input().strip()))
    print(direction)