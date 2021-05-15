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
    print(maxv, minv)

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
            m_14888_recur(num - lst[idx], idx + 1, add, sub - 1, multi, division, n, lst, maxv, minv)
        if multi:
            m_14888_recur(num * lst[idx], idx + 1, add, sub, multi - 1, division, n, lst, maxv, minv)
        if division:
            m_14888_recur(-(-num // lst[idx]) if num < 0 else num // lst[idx], idx + 1, a, s, m, d - 1)


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

import sys
from heapq import heappush, heappop

def m_1916():
    n = int(input())
    m = int(input())
    bus = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        bus[start].append((end, cost))
    start, end = map(int, input().split())

    print(m_1916_dijkstra(start, end, n, bus))

def m_1916_dijkstra(start, end, n, bus):
    heap = []
    heappush(heap, (0, start))
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0

    while heap:
        weight, index = heappop(heap)
        for e, c in bus[index]:
            if distance[e] > weight + c:
                distance[e] = weight + c
                heappush(heap, (weight + c, e))
    return distance[end]


def m_1197(): ### 벨만포드 뼈대 문제
    v, e = map(int, input().split())
    edge = []
    for _ in range(e):
        a, b, w = map(int, input().split())
        edge.append((w, a, b))
    edge.sort(key=lambda x: x[0])

    parent = list(range(v + 1))

    result = 0
    for w, s, e in edge:
        if m_1197_find(s, parent) != m_1197_find(e, parent):
            m_1197_union(s, e, parent)
            result += w
    print(result)

def m_1197_union(a, b, parent):
    a = m_1197_find(a, parent)
    b = m_1197_find(b, parent)

    if b < a:
        parent[a] = b 
    else:
        parent[b] = a

def m_1197_find(a, parent):
    if a == parent[a]:
        return a
    parent[a] = m_1197_find(parent[a], parent) 
    return parent[a]


def m_16916(): ### KMP 알고리즘
    s = input()
    p = input()

    pi = [0 for x in range(len(p))]
    if m_16916_kmp(s, p, pi):
        print('1')
    else:
        print('0')

def m_16916_getPI(pattern, pi):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def m_16916_kmp(s, pattern, pi):
    m_16916_getPI(pattern, pi)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False


def m_2252(): ### 위상정렬
    n, m = map(int, input().split())
    students = [0 for _ in range(n)]
    heights = {}
    for _ in range(m):
        a, b = map(int, input().split())
        students[b - 1] += 1
        if a - 1 in heights:
            heights[a - 1].append(b - 1)
        else:
            heights[a - 1] = [b - 1]

    queue = deque()
    for i in range(n):
        if students[i] == 0:
            queue.append(i)

    result = []
    while queue:
        i = queue.popleft()
        result.append(i + 1)
        if i in heights:
            for j in heights[i]:
                students[j] -= 1
                if students[j] == 0:
                    queue.append(j)
    print(*result)            


# m_14888()
# m_2504()
# m_14719()
# m_1062()
# m_1700()
# m_1806()
# m_1916()
# m_1197()
m_16916()
# m_2252()