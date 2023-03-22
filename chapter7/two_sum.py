# First Solution


# 브루트 포스 방식 -> 비효율!!
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Second Solution


# 브루트 포스와 시간복잡도는 같지만, 파이썬 내부 함수로 구현된 in이 훨씬 가벼움
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, num in enumerate(nums):
            remains = target - num
            if remains in nums[index + 1 :]:
                return [index, nums[index + 1 :].index(remains) + (index + 1)]


# Third Solution


# dictionary는 해시 테이블을 조회하기 때문에, 평균적으로 O(1)(최악의 경우 O(n))에 조회가 가능하다.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for index, value in enumerate(nums):
            if target - value in nums_map and index != nums_map[target - value]:
                return [index, nums_map[target - value]]
            nums_map[value] = index
