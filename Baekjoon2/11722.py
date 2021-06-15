### 가장 긴 감소하는 부분 수열
n = int(input())
a = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1: a[i] = 1
    if i == 2: a[i] = 2
    else:
        a[i] = a[i - 1] + a[i - 2]

print(a[n] % 10007)