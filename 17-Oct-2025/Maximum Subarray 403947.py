# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)
        prefix = 0
        for num in nums:
            prefix += num
            result = max(result, prefix)
            
            if prefix < 0:
                prefix = 0

        return result