### 파일 합치기
import sys
tc = int(input())

read = sys.stdin.readline
MAX = sys.maxsize

def solution():
    n=int(read())
    num=list(map(int,read().split()))

    dp=list(list(0 for _ in range(n)) for _ in range(n))
    #if n=5
    for k in range(1,n):#k=1,2,3,4
        for i in range(n-k):#i=0,1,2,3,4 when k=1
            X,Y=i,i+k
            dp[X][Y]=MAX
            for j in range(k):
                tmp=dp[X+1+j][Y]+dp[X][Y-k+j]
                dp[X][Y]=min(dp[X][Y],tmp)
            dp[X][Y]+=sum(num[X:Y+1])
    print(dp[0][-1])


def solution2():
    n = int(input())
    file = list(map(int, input().split()))
    dp = [[0] * (n) for _ in range(n)]
    knuth = [[0] * (n) for _ in range(n)]
    for i in range(n):
        knuth[i][i] = i
    
    for x in range(1, n):
        for i in range(n - x):
            j = x + i
            dp[i][j] = MAX
            tmp = sum(file[i : j+1])
            for k in range(knuth[i][j - 1], knuth[i + 1][j] + 1):
                if k < n - 1 and dp[i][j] > dp[i][k] + dp[k + 1][j] + tmp:
                    dp[i][j] = dp[i][k] + dp[k + 1][j] + tmp
                    knuth[i][j] = k
    print(dp[0][n - 1])


for i in range(tc):
    solution2()