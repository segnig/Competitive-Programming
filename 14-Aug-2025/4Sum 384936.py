# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                temp = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if temp + nums[right] + nums[left] == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        right -= 1
                        left += 1
                    elif temp + nums[right] + nums[left] > target:
                        right -= 1
                    else:
                        left += 1

        return list(result)
