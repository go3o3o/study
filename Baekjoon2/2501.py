### 약수 구하기
n, k = map(int, input().split())

result = [1]

for i in range(2, n + 1):
    if n % i == 0:
        result.append(i)

if len(result) < k:
    print(0)
else:
    print(result[k - 1])