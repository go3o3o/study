s = input()
p = input()

pi = [0 for _ in range(len(p))]

def getPI(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - i]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def kmp(s, pattern):
    getPI(pattern)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

if kmp(s, p):
    print('1')
else:
    print('0')


"""
baekjoon
aek
-> 1

baekjoon
bak
-> 0

baekjoon
joo
-> 1

baekjoon
oone
-> 0
"""