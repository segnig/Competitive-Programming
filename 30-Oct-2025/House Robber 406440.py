# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dp(index):
            if index >= len(nums):
                return 0
            if index not in memo:
                take = nums[index] + dp(index + 2)
                not_take = dp(index + 1)

                memo[index] = max(take, not_take)
            return memo[index]

        return dp(0)