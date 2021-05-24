### N-Queen
import sys

def dfs(i):
    global n, col, slash, backslash, case
    if i == n:
        case += 1
        return
    for j in range(n):
        if not (col[j] or slash[i + j] or backslash[i - j + n - 1]):
            col[j] = slash[i + j] = backslash[i - j + n - 1] = True
            dfs(i + 1)
            col[j] = slash[i + j] = backslash[i - j + n - 1] = False

n = int(input())
col, slash, backslash = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
case = 0
dfs(0)
print(case)