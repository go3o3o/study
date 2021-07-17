### 문자열 폭팔
letter = input()
bomb = input() 
bomb_lst = list(bomb)
bomb_last = bomb[-1]
bomb_len = len(bomb)

ans = []
for i in letter:
    ans.append(i)
    print(bomb_lst, ans[-bomb_len:])
    if bomb_last == i and bomb_lst == ans[-bomb_len:]:
        
        del ans[-bomb_len:]
print(''.join(ans) if ans else "FRULA")