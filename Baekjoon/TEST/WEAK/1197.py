v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, w = map(int, input().split())
    edge.append((w, a, b))
edge.sort(key = lambda x : x[0])

parent = list(range(v + 1))

result = 0


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a 

for w, s, e in edge:
    if find(s) != find(e):
        union(s, e)
        result += w
print(result)

"""
3 3
1 2 1
2 3 2
1 3 3
-> 3
"""