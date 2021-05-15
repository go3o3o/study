import sys

maxv = -sys.maxsize - 1
minv = sys.maxsize


def recursive(num, idx, a, s, m, d):
    global maxv, minv
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        
        return
    else:
        if a:
            recursive(num + lst[idx], idx + 1, a - 1, s, m, d)
        if s:
            recursive(num - lst[idx], idx + 1, a, s - 1, m, d)
        if m:
            recursive(num * lst[idx], idx + 1, a, s, m - 1, d)
        if d:
            recursive(-(-num // lst[idx]) if num < 0 else num // lst[idx], idx + 1, a, s, m, d - 1)

n = int(input())
lst = list(map(int, input().split()))
a, s, m, d = list(map(int, input().split()))
recursive(lst[0], 1, a, s, m, d)
print(maxv, minv)