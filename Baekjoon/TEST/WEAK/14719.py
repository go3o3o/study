h, w = map(int, input().split())
drop = list(map(int, input().split()))

result = 0
for i in range(len(drop)):
    max_left = max(drop[:i + 1])
    max_right = max(drop[i:])

    which_low = min(max_left, max_right)
    print(max_left, max_right, which_low)
    result += abs(drop[i] - which_low)
print(result)

"""
4 4
3 0 1 4
-> 5

4 8
3 1 2 3 4 1 1 2
-> 5

3 5
0 0 0 2 0
-> 0
"""