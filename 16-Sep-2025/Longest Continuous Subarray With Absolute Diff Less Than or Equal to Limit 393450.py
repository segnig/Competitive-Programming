# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = -1
        result = 1

        for right in range(len(nums)):
            while decreasing and decreasing[-1][0] < nums[right]:
                decreasing.pop()

            decreasing.append((nums[right], right))
            while increasing and increasing[-1][0] > nums[right]:
                increasing.pop()
                
            increasing.append((nums[right], right))
            while decreasing and abs(decreasing[0][0] - nums[right]) > limit:
                popped = decreasing.popleft()
                left = max(left, popped[1])
            while increasing and abs(increasing[0][0] - nums[right]) > limit:
                popped = increasing.popleft()
                left = max(left, popped[1])
            result = max(result, right - left)
        return result