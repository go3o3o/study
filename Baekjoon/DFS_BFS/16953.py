### A -> B

a, b = map(int, input().split()) 
queue = [(b, 1)]
result = -1
while queue:
    x, cnt = queue.pop(0)
    if x == a:
        result = cnt 
        break

    if x % 2 == 0 and x // 2 >= a:
        queue.append((x / 2, cnt + 1))
    elif x % 10 == 1 and x // 10 >= a:
        # print(int(x / 10), x // 10)
        queue.append((x // 10, cnt + 1))
    else:
        break
print(result)