### 숫자 야구
from itertools import permutations

n = int(input())
num = list(permutations(range(1, 10), 3))

def check(num, ans):
    strike = 0
    ball = 0
    for i in range(3):
        if str(num[i]) == ans[i]: strike += 1
        elif str(num[i]) in ans: ball += 1 
    return (strike, ball)

for _ in range(n):
    ans, s, b = map(int, input().split())
    result = []
    for i in num:
        tstrike, tball = check(i, str(ans))
        if tstrike == s and tball == b:
            result.append(i)
    num = result
# print(num)
print(len(num))