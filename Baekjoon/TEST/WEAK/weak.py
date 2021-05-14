from collections import deque

import sys
input = sys.stdin.readline

def m_14888(): ### 재귀탐색
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


def m_2504(): ### 스택
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


def m_14719(): ### 시뮬레이션
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

import sys
from itertools import combinations

def m_1062(): ### 완전탐색
    n, k = map(int, input().split())
    basic_set = {'a', 'c', 'i', 'n', 't'}
    all_set = set()
    word_lst = []
    ans = 0
    for _ in range(n):
        word_set = set(sys.stdin.readline())
        word_set = word_set - {'\n'}
        print(word_set)
        diff_set = word_set - basic_set
        print(diff_set)
        word_lst.append(list(diff_set))

        all_set = all_set.union(word_set)
    diff_set = all_set - basic_set
    diff_lst = list(diff_set)
    diff_lst = sorted(diff_lst)
    per = combinations(diff_lst, k - 5)

    for spellin in per:
        cnt = 0
        spell_lst = list(spellin) # 알려줄 알파벳 리스트
        for word_gp in word_lst: #[[r], [c,a,r]] 리스트에서
            isTrue = 1
            for word in word_gp: # [c,a,r] -> c, 실제 단어
                if word in spell_lst:
                    isTrue *= 1
                else:
                    isTrue *= 0
            if isTrue == 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)


def m_1700(): ### 그리디
    n, k = map(int, input().split())
    multitap = list(map(int, input().split()))

    plugs = []
    count = 0
    for i in range(k):
        if multitap[i] in plugs:
            continue
        # 플러그가 비어 있으면 꼽기
        if len(plugs) < n:
            plugs.append(multitap[i])
            continue
        multitap_idxs = []
        hasplug = True

        for j in range(n):
            if plugs[j] in multitap[i:]:
                multitap_idx = multitap[i:].index(plugs[j])
            else:
                multitap_idx = 101
                hasplug = False
            multitap_idxs.append(multitap_idx)

            if not hasplug:
                break
        
        # 플러그를 뽑는다
        plug_out = multitap_idxs.index(max(multitap_idxs))
        del plugs[plug_out]
        plugs.append(multitap[i])
        count += 1
    print(count)


def m_1806(): ### 투포인터
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    sum_a = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_a[i] = sum_a[i - 1] + a[i - 1]

    answer = 1000001
    start = 0
    end = 1

    while start != n:
        if sum_a[end] - sum_a[start] >= s:
            if end - start < answer:
                answer = end - start
            start += 1
        else:
            if end != n:
                end += 1
            else: 
                start += 1

    if answer != 100001:
        print(answer)
    else:
        print(0)


# m_14888()
# m_2504()
# m_14719()
# m_1062()
# m_1700()
m_1806()