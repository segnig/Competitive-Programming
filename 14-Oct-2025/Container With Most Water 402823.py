# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1

        result = 0

        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return result