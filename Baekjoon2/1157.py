### 단어 공부 
word = list(input().upper())
word_set = list(set(word))

result = []
for i in word_set:
    count = word.count(i)
    result.append(count)

if result.count(max(result)) > 1:
    print('?')
else:
    max_index = result.index(max(result))
    print(word_set[max_index])