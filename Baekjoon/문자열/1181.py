### 단어 정렬
n = int(input())

dictionary = []
for _ in range(n):
    word = input()
    dictionary.append((len(word), word))

dictionary = list(set(dictionary))

print(dictionary)
dictionary.sort(key = lambda word: (word[0], word[1]))
print(dictionary)