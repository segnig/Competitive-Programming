# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[0], nums[1])
            
            rob = nums[i] + dp(i - 2)
            dont_rob = dp(i - 1)

            return max(rob, dont_rob)
        
        return dp(len(nums) - 1)