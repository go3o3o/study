### 단어 공부
alphabet = input().upper()
alphabet_set = list(set(alphabet))

cnt_lst = []
for i in alphabet_set:
    cnt = alphabet.count(i)
    cnt_lst.append(cnt)

# print(cnt_lst)
# print(cnt_lst.count(max(cnt_lst)))
if cnt_lst.count(max(cnt_lst)) > 1:
    print('?')
else:
    max_index = cnt_lst.index(max(cnt_lst))
    # print(max_index)
    print(alphabet_set[max_index])
