from collections import deque

n, m = map(int, input().split())
students = [0 for _ in range(n)]
heights = {}

for _ in range(m):
    a, b = map(int, input().split())
    students[b - 1] += 1
    if a - 1 in heights:
        heights[a - 1].append(b - 1)
    else:
        heights[a - 1] = [b - 1]
    
queue = deque()
for i in range(n):
    if students[i] == 0:
        queue.append(i)

result = []
while queue:
    i = queue.popleft()
    result.append(i + 1)
    for i in heights:
        for j in heights[i]:
            students[j] -= 1
            if students[j] == 0:
                queue.append(j)
print(*result)

"""
3 2
1 3
2 3
-> 1 2 3

4 2 
4 2
3 1
-> 4 2 3 1
"""