### 싸이버개강총회
from sys import stdin

개총시작시간, 개총끝난시간, 스트리밍끝난시간 = map(str, input().split())
개총시작시간 = int("".join(개총시작시간.split(":")))
개총끝난시간 = int("".join(개총끝난시간.split(":")))
스트리밍끝난시간 = int("".join(스트리밍끝난시간.split(":")))
개총시작전에채팅친사람들 = {}
count = 0
while(True):
  line = stdin.readline()
  if len(line) < 5: break ' 마지막에 있는 빈줄을 대응해준다
  t, _id = map(str, line.split())
  t = int("".join(t.split(":")))
  if t <= 개총시작시간: 개총시작전에채팅친사람들[_id] = 1
  elif 개총끝난시간 <= t <= 스트리밍끝난시간:
    if 개총시작전에채팅친사람들.get(_id) == 1:
      # 이미 카운팅 했음을 표시해준거임
      개총시작전에채팅친사람들[_id] = 개총시작전에채팅친사람들[_id] + 1 
      count += 1
print(count)