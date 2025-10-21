# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for index, num in enumerate(nums):
            if target - num in store:
                return [store[target - num], index]
            store[num] = index