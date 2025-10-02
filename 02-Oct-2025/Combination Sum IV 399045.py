# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(total):
            if total == 0:
                return 1
            if total < 0:
                return 0
            result = 0
            for num in nums:
                result += dp(total-num)
            
            return result
        
        return dp(target)