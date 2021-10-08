# https://leetcode.com/problems/reverse-string/

def reverseStringUsingTwoPointer(self, s: [str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverseString(self, s: [str]) -> None:
    s.reverse()