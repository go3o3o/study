### 숫자 야구
from itertools import permutations

n = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(n):
    ans, s, b = map(int, input().split())
    ans = list(str(ans))
    remove_cnt = 0

    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= remove_cnt

        for j in range(3):
            ans[j] = int(ans[j])
            if ans[j] in num[i]:
                if j == num[i].index(ans[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
            if s_cnt != s or b_cnt != b:
                num.remove(num[i])
                remove_cnt += 1

print(len(num))