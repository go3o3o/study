# https://leetcode.com/problems/group-anagrams/
import collections

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬화하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())