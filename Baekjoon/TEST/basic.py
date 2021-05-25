def m_2501():
    n, k = map(int, input().split())
    divisor = [1, n]
    for i in range(2, n):
        if n % i == 0:
            divisor.append(i)
    divisor.sort()
    print(divisor[k - 1])

def m_3460():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = bin(n)[2:]
        for i in range(len(b)):
            if b[::-1][i] == '1':
                print(i, end=' ')
                        
def m_2693():
    t = int(input())
    for _ in range(t):
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        print(a[2])



# m_2501()
# m_3460()
m_2693()