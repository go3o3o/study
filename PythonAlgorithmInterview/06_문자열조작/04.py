# https://leetcode.com/problems/most-common-word/
import collections
import re


def mostCommontWord(self, paragraph: str, banned: [str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]

    counts = collections.Counter(words)

    # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
    return counts.most_common(1)[0][0]