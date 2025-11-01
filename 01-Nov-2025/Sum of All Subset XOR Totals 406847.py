# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        result = 0
        def backtrack(index, xor=0):
            nonlocal result
            if index == len(nums):
                result += xor
                return
            backtrack(index + 1, xor ^ nums[index])
            backtrack(index + 1, xor)
        backtrack(0)

        return result