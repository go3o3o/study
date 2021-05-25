### N번째 큰 수 

tc = int(input())
for _ in range(tc):
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    print(a[2])