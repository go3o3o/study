### 1로 만들기
n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        continue
    values = []
    if i % 3 == 0:
        values.append(dp[i//3] + 1)
    if i % 2 == 0:
        values.append(dp[i//2] + 1)
    values.append(dp[i - 1] + 1)

    dp[i] = min(values)

print(str(dp[n]))
    