# https://leetcode.com/problems/two-sum/

def twoSumUsingBruteForce(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSumUsingIn(self, nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


def twoSumUsingDict(self, nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

def twoSumUsingDict2(self, nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i