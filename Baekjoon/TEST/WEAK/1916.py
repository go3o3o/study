import sys
from heapq import heappush, heappop

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    bus[start].append((end, cost))
start, end = map(int, input().split())

def dijkstra(start, end):
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

print(dijkstra(start, end))



"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
-> 4
"""