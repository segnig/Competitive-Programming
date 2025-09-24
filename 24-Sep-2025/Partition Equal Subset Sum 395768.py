# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2

        @cache
        def dp(idx, sub1):
            if idx == len(nums):
                return target == sub1

            return dp(idx + 1, sub1 + nums[idx]) or dp(idx + 1, sub1)

        return dp(0, 0)