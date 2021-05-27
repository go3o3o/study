### 단어 정렬
import sys
n = int(input())
words = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append((len(word), word))

words = list(set(words))
result = sorted(words, key=lambda word: (word[0], word[1]))
for i in result:
    print(i[1])