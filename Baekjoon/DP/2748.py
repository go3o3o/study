### 피보나치 수 2
n = int(input())
a = [i for i in range(n + 1)]
a[1] = 1

for i in range(2, n + 1):
    a[i] = a[i - 1] + a[i - 2]

print(a[-1])