### 숨바꼭질 2
from collections import deque
n, k = map(int, input().split())
MAX= 100001

queue = deque()
queue.append(n)

result = 0
visited = [-1] * MAX
visited[n] = 0

while queue:
    now_pos = queue.popleft()

    if now_pos == k:
        result += 1
    for next_pos in [now_pos * 2, now_pos + 1, now_pos - 1]: 
        if 0 <= next_pos < MAX:
            if visited[next_pos] == -1 or visited[next_pos] >= visited[now_pos] + 1:
                visited[next_pos] = visited[now_pos] + 1
                queue.append(next_pos)

print(visited[k])
print(result)