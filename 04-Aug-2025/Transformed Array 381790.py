# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                result[i] = nums[(nums[i] + i) % len(nums)]
            elif nums[i] < 0:
                result[i] = nums[(nums[i] + i) % len(nums)]

        return result

        