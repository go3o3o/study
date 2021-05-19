### 암호 만들기 
### 백트래킹
import sys
import sys
from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
password = sorted(list(map(str, sys.stdin.readline().split())))
comb = combinations(password, l)

for c in comb:
    count = 0
    for letter in c:
        if letter in vowel:
            count += 1
    if (count >= 1) and (count <= l - 2):
        print(''.join(c))