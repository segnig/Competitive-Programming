# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = 0

        @cache
        def dp(index, current):
            nonlocal total
            if index == len(nums):
                return current == target
                
            else:
                return dp(index + 1, current + nums[index]) + dp(index + 1, current - nums[index])

        return dp(0, 0)
        
            