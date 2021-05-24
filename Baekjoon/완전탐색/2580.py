### 스도쿠
import sys
sudoku = [list(map(int, input().split())) for _ in range(9)]
# print(sudoku)

zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
# print(zeros)

def is_promising(i, j):
    promising = [i for i in range(1, 10)]

    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])

    i //= 3
    j //= 3
    for p in range(i * 3, (i+1) * 3):
        for q in range(j * 3, (j+1) * 3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    return promising

flag = False
def dfs(x):
    global flag
    if flag: return
    
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return

    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)

        for num in promising:
            sudoku[i][j] = num
            dfs(x + 1)
            sudoku[i][j] = 0

dfs(0)

