# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dp(index):
            if index == len(nums):
                return 0
            
            take = 1
            for i in range(index + 1, len(nums)):
                if nums[index] < nums[i]:
                    take = max(take, 1 + dp(i))

                
    
            return take
        result = 1

        for i in range(len(nums)):
            result = max(result, dp(i))

        return result
        
