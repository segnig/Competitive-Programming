# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for index, num in enumerate(nums):
            if target - num in s:
                return [s[target - num], index]
            s[num] = index
        return []