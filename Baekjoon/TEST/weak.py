from collections import deque

import sys
input = sys.stdin.readline

def m_14888():
    maxv = -sys.maxsize - 1
    minv = sys.maxsize
    n = int(input())
    lst = list(map(int, input().split()))
    a, s, m, d = list(map(int, input().split())) # +, -, *, /
    recur_14888(lst[0], 1, a, s, m, d, n, lst, maxv, minv)

def recur_14888(num, idx, add, sub, multi, division, n, lst, maxv, minv):
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        print(maxv, minv)
        return 
    else:
        if add:
            recur_14888(num + lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)
        if sub:
            recur_14888(num - lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)
        if multi:
            recur_14888(num * lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)
        if division:
            recur_14888(num // lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)


m_14888()