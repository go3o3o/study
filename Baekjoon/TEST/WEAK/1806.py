n, s = map(int, input().split())
a = list(map(int, input().split()))

sum_a = [0] * (n + 1)
for i in range(1, n + 1):
    sum_a[i] = sum_a[i - 1] + a[i - 1]
result = 1000001
start = 0
end = 1

while start != n:
    if sum_a[end] - sum_a[start] >= s:
        if end - start < result:
            result = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1
if result != 1000001:
    print(result)
else:
    print(0)

"""
10 15
5 1 3 5 10 7 4 9 2 8
-> 2
"""