### 프린터 큐
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    important = list(map(int, input().split()))
    idx = list(range(len(important)))

    idx[m] = 'target'

    order = 0

    while True:
        if important[0] == max(important):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                important.pop(0)
                idx.pop(0)

        else:
            important.append(important.pop(0))
            idx.append(idx.pop(0))
