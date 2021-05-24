### 문자열 폭발
import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()
word_len = len(word)
bomb_len = len(bomb)

last_char = bomb[-1]

stack = []
for w in word:
    stack.append(w)
    if w == last_char and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

# print(stack)
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))