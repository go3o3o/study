### 일곱 난쟁이 
from itertools import combinations

dwarf = [int(input()) for _ in range(9)]
occation = list(combinations(dwarf, 7))

# print(occation)

for i in occation:
    if sum(i) == 100:
        answer = list(i)
        break

answer.sort()
print('\n'.join(str(x) for x in answer))
