# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = [1]* len(nums)

        base = 1
        m =1
        while base < len(nums):
            gg = 0
            
            
            while gg < base:
                if nums[gg] < nums[base]:
                    count[base] = max(count[base], count[gg] + 1)
                    m = max(count[base], m)

                gg+=1

            base += 1
        return m