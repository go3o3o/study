# https://www.acmicpc.net/problem/2484
def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]: return 10000 + lst[1] * 1000
        return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        if lst[i] == lst[i+1]: return 1000 + lst[i] * 100
    return lst[-1] * 100

num = int(input())
print(max(money() for _ in range(num)))