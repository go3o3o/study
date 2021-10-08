# https://leetcode.com/problems/array-partition-i/

def arrayPairSum(self, nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


def arrayPairSum(self, nums: list[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum


def arrayPairSum(self, nums: list[int]) -> int:
    return sum(sorted(nums)[::2])
