### 로또
from itertools import combinations
strategies = []

while True:
    try: 
        strategy = list(map(int, input().split()))
        if strategy == [0]: break
    except EOFError: break
    strategies.append(strategy)

for strategy in strategies:
    k, s = strategy[0], strategy[1:]
    result = combinations(s, 6)
    for i in result:
        print(*list(i))
    print()
