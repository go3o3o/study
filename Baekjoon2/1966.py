### 프린터 큐
from collections import deque 

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    important = list(map(int, input().split()))
    checked = [0 for _ in range(n)]
    checked[m] = 1

    count = 0
    while True:
        if important[0] == max(important):
            count += 1 

            if checked[0] != 1:
                del important[0]
                del checked[0]
            else:
                print(count)
                break
        else:
            important.append(important[0])
            checked.append(checked[0])
            del important[0]
            del checked[0]
