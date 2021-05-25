### 숨바꼭질 2
import sys
from collections import deque
n, k = map(int, input().split())
MAX_SIZE = 100001

queue = deque()
queue.append(n)

result = 0
visited = [-1] * MAX_SIZE
visited[n] = 0
while queue: 
    x = queue.popleft()

    if x == k:
        result += 1
    for i in [x * 2, x + 1, x - 1]:
        if 0 <= i < MAX_SIZE:
            print(visited[i])
            print(visited[x])
            if visited[i] == -1 or visited[i] >= visited[x] + 1:
                visited[i] = visited[x] + 1
                queue.append(i)

print(visited[k])
print(result)