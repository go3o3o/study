### 암호 만들기 
import sys
from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())

word = input().split()
combinations = combinations(sorted(word), l)

result = []
for comb in combinations:
    vowel_cnt = 0
    consonant_cnt = 0
    for i in comb:
        if i in vowel:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

    if (vowel_cnt >= 1 and consonant_cnt >= 2):
        print(''.join(comb))
