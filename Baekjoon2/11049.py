### 행렬 곱셈 순서
n = int(input())
li=[0]
for _ in range(n) :
    li.append(list(map(int,input().split())))

gr = [[0]*(n+1) for i in range(n+1)]

for j in range(2,n+1) :
    for i in range(j-1,0,-1) :
        mi = 2**31
        for k in range(i,j) :
            x = gr[i][k] + gr[k+1][j] + li[i][0]*li[k][1]*li[j][1]
            if x < mi :
                mi = x
        gr[i][j] = mi
print(gr[1][n])
                