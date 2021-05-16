import sys
from itertools import combinations

n, k = map(int, input().split())
basic_set = {'a', 'c', 'i', 'n', 't'}
all_set = set()
word_lst = []
result = 0
for _ in range(n):
    word_set = set(sys.stdin.readline())
    word_set = word_set - {'\n'}
    diff_set = word_set - basic_set
    word_lst.append(list(diff_set))
    print(all_set, word_set)
    all_set = all_set.union(word_set)

diff_set = all_set - basic_set
diff_lst = list(diff_set)
diff_lst = sorted(diff_lst)

print(diff_lst)
per = combinations(diff_lst, k - 5)

for spell in per:
    print(spell)
    cnt = 0
    spell_lst = list(spell)
    for word_gp in word_lst:
        isTrue = 1
        for word in word_gp:
            if word in spell_lst:
                isTrue *= 1
            else:
                isTrue *= 0
        if isTrue == 1:
            cnt += 1
    result = max(result, cnt)
print(result)

"""
3 6
antarctica
antahellotica
antacartica
-> 2

2 3
antaxxxxxxxtica
antarctica
-> 0

9 8
antabtica
antaxtica
antadtica
antaetica
antaftica
antagtica
antahtica
antajtica
antaktica
-> 3
"""