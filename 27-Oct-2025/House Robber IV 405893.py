# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def checker(mid):
            count = 0
            index = 0
            max_val = -inf

            while index < len(nums):
                if nums[index] <= mid:
                    max_val = max(max_val, nums[index])
                    count += 1
                    index += 2
                else:
                    index += 1
            return count >= k, max_val

        
        left = min(nums)
        right = max(nums)
        answer = right
        while left < right:
            mid = left + (right - left)// 2

            is_possible, val = checker(mid)
            if is_possible:
                right = mid - 1
                answer = val
            else:
                left = mid + 1

        return answer
            