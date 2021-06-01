### 숨바꼭질
from collections import deque
MAX = 100001
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

n, k = map(int, input().split())

result = [0] * MAX

def bfs():
    queue = deque([n])
    while queue:
        now_pos = queue.popleft()
        if now_pos == k:
            return result[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < MAX and not result[next_pos]:
                result[next_pos] = result[now_pos] + 1
                queue.append(next_pos)
print(bfs())