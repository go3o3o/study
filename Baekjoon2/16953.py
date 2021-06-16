### A -> B 

a, b = map(int, input().split())
count = 1

while b > a:
    count += 1 
    if b % 10 == 1:
        b //= 10 
    elif b % 2:
        break 
    else:
        b //= 2

print(count if a == b else -1)