# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        Sum = 0
        for num in nums:
            Sum ^= num
        
        ans = 0
        k ^= Sum 
        while k > 0:
            ans += k & 1
            k >>= 1
        
        return ans        