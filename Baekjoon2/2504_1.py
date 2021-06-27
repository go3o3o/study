s = list(input())
q = []
error_flag = False

for i in range(len(s)):
    if s[i] == '(' or s[i] == '[':
        q.append(s[i])
        continue
    elif s[i] == ')':
        val = 2
        true_left = '('
        false_left = '['
    elif s[i] == ']':
        val = 3
        true_left = '['
        false_left = '('

    tmp = 0
    while True:
        if len(q) == 0:
            error_flag = True
            break

        x = q.pop()
        if x == true_left:
            break
        elif x == false_left:
            error_flag = True
            break
        else:
            tmp += x

    tmp = val if tmp == 0 else tmp * val
    q.append(tmp)

if '(' in q or '[' in q:
    error_flag = True

print(0) if error_flag else print(sum(q))