### 이진수

tc = int(input())
for _ in range(tc):
    n = format(int(input()), 'b')
    n = str(n)
    # lst = [i if i == '1' else 0 for i in n]
    for idx, i in enumerate(n):
        if i == '1':
            print(idx, end=' ')
   