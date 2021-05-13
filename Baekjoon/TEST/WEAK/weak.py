from collections import deque

import sys
input = sys.stdin.readline

def m_14888():
    maxv = -sys.maxsize - 1
    minv = sys.maxsize
    n = int(input())
    lst = list(map(int, input().split()))
    a, s, m, d = list(map(int, input().split())) # +, -, *, /
    m_14888_recur(lst[0], 1, a, s, m, d, n, lst, maxv, minv)

def m_14888_recur(num, idx, add, sub, multi, division, n, lst, maxv, minv):
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        print(maxv, minv)
        return 
    else:
        if add:
            m_14888_recur(num + lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)
        if sub:
            m_14888_recur(num - lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)
        if multi:
            m_14888_recur(num * lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)
        if division:
            m_14888_recur(num // lst[idx], idx + 1, add - 1, sub, multi, division, n, lst, maxv, minv)


def m_2504():
    sb = list(input())
    # print(sb)
    stack = list()
    for i in sb:
        if i == ")":
            temp = 0
            while stack:
                top = stack.pop()
                if top == "(":
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * temp)
                    break
                elif top == "[":
                    print("0")
                    # exit(0)
                else:
                    if temp == 0:
                        temp = int(top)
                    else:
                        temp = temp + int(top)
        elif i == "]":
            temp = 0
            while stack:
                top = stack.pop()
                if top == "[":
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * temp)
                    break
                elif top == "(":
                    print("0")
                    # exit(0)
                else:
                    if temp == 0:
                        temp = int(top)
                    else:
                        temp = temp + int(top)
        else:
            stack.append(i)
        print(stack)
    result = 0
    print(stack)
    for i in stack:
        if i == "(" or i == "[":
            print(0)
            exit(0)
        else:
            result += i
    print(result)
    pass 


def m_14719():
    h, w = map(int, input().split())
    drop = list(map(int, input().split()))
    raindrop = 0
    for i in range(len(drop)):
        # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이
        max_left = max(drop[:i + 1])
        # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이
        max_right = max(drop[i:])

        which_low = min(max_left, max_right)
        raindrop = raindrop + abs(drop[i] - which_low)
    print(raindrop)

    

# m_14888()
# m_2504()
m_14719()