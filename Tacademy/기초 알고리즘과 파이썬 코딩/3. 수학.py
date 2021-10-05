# 최대공약수
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# 유클리드 호제법
def euclidean(a, b):
    return b if a%b == 0 else gcd(b, a%b)

# 소수 체크
def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True

# 에라토스테네스의 체 
def era(n):
    ck, p = [False for _ in range(n+1)], []
    for i in range(2, n+1):
        if ck[i] == True: continue
        p.append(i)
        for j in range(i*i, n+1, i):
            ck[j] = True
    return ck, p

# 하노이탑
def hanoi(start, end, size):
    if size == 1: return print(start, end)
    hanoi(start, 6-start-end, size-1)
    print(start, end)
    hanoi(6-start-end, end, size-1)

n = int(input())
print(2**n-1)
hanoi(1, 3, n)