# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        counter = 0

        for num in nums:
            if counter == 0:
                ans = num
            if ans == num:
                counter += 1
            else:
                counter -= 1
        
        return ans
        