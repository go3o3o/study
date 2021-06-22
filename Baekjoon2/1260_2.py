import sys
sys.setrecursionlimit(10**6)

def dfs(V):
    visit[V] = 1
    result1.append(V)
    for i in board[V]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)

def bfs(V):
    visit = [0] * (N + 1)
    visit[V] = 1
    result2.append(V)
    tmp = [V]
    while tmp:
        q = tmp.pop(0)
        for i in board[q]:
            if visit[i] == 0:
                result2.append(i)
                tmp.append(i)
                visit[i] = 1
        

N, M, V = map(int, sys.stdin.readline().split())
board = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
for i in range(len(board)):
    board[i].sort()
visit = [0] * (N + 1)
result1 = []
result2 = []
dfs(V)
bfs(V)
print(*result1)
print(*result2)