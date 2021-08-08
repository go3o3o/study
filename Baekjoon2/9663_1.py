# N-Queen

n = int(input())
count = 0
row = [0 for _ in range(n)]
left = [0 for _ in range(2 * n-1)]
right = [0 for _ in range(2 * n-1)]

def dfs(i):
    global count
    if i == n:
        count += 1
        return
    for j in range(n): # 열을 이동하며
        if row[j] + left[i + j] + right[n - 1 + i - j] == 0:
            row[j] = left[i + j] = right[n - 1 + i - j] = 1
            dfs(i + 1)
            row[j] = left[i + j] = right[n - 1 + i - j] = 0

dfs(0)
print(count)

