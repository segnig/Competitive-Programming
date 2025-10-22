# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        store = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in store:
                result.append(i)
        
        return result