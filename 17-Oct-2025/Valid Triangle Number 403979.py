# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        result = 0
        nums.sort()

        for c in range(2, len(nums)):
            a, b = 0, c-1
            while a < b:
                if nums[a]+nums[b] > nums[c]:
                    result += b - a
                    b -= 1
                else:
                    a += 1
        return result