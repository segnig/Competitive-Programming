# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incr = deque()
        decreasing = deque()
        left = -1
        result = 1

        for right in range(len(nums)):
            while decreasing and decreasing[-1][0] < nums[right]:
                decreasing.pop()

            decreasing.append((nums[right], right))
            while incr and incr[-1][0] > nums[right]:
                incr.pop()
                
            incr.append((nums[right], right))
            while decreasing and abs(decreasing[0][0] - nums[right]) > limit:
                popped = decreasing.popleft()
                left = max(left, popped[1])
            while incr and abs(incr[0][0] - nums[right]) > limit:
                popped = incr.popleft()
                left = max(left, popped[1])
            result = max(result, right - left)
        return result