
# 1. 문자열 거꾸로 하기
from typing import Counter


def reverseString(self):
    string = "ABCDE"
    result = string[::-1]

# 2. title case 사용
def titleCase(self):
    string = "my name is yonikim"
    result = string.title()

# 3. 문자열에서 중복 글자 제거
def removeDuplicateString(self):
    string = "aabbcccdddddee"
    temp_set = set(string)
    result = ''.join(temp_set)

# 4. 리스트 Comprehension
def comprehension(self):
    original_list = [1, 2, 3, 4]
    result = [2 * x for x in original_list]

# 5. 주어진 문자열이 Palindrome 인지 판단
def checkPalindrome(self):
    string = "abcd"
    if string == string[::-1]: return True
    else: return False

# 6. 리스트의 각 엘리먼트의 반복 횟수 구하기
def countElement(self):
    my_list = ['a', 'a', 'b', 'b', 'b', 'c']
    count = Counter(my_list)

    print(count['b'])
    print(count.most_common(1))

# 7. 두 문자열이 Anagrams 인지 확인
def checkAnagrams(self):
    string_1, string_2 = "acbde", "abced"
    count_1, count_2 = Counter(string_1), Counter(string_2)

    if count_1 == count_2: return True
    else: return False

# 8. 객체의 메모리 사용량 확인
def checkMemoryUsage(self):
    import sys
    num = 21
    print(sys.getsizeof(num))
    string = 'python'
    print(sys.getsizeof(string))

# 9. 두 딕셔너리 병합 
def combineDictionry(self):
    dict_1 = { 'apple': 9, 'banana': 6 }
    dict_2 = { 'banana': 4, 'orange': 10 }

    combined_dict = {**dict_1, **dict_2}

# 10. 중복 리스트 플랫화
from iteration_utilities import deepflatten
def flatten(self, my_list):
    return [item for sublist in my_list for item in sublist]
def flattenList(self):
    my_list = [[1, 2, 3], [3]]
    print(flatten(my_list))

    my_list2 = [[1, 2, 3], [4, [5], [6, 7]], [8, [9, [10]]]]
    print(list(deepflatten(my_list2, depth=3)))
    
