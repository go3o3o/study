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
        x = int(input())
        b = list(format(x, 'b'))
        for idx, i in enumerate(b):
            if i == '1':
                print(idx, end=' ')
        
def m_2693():
    t = int(input())
    for _ in range(t):
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        print(a[2])



# m_2501()
# m_3460()
m_2693()