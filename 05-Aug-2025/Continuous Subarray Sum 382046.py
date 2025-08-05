# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = []
        hash_map = {0:-1}

        for i, num in enumerate(nums):
            if not pre_sum:
                pre_sum.append(num % k)
            else:
                pre_sum.append((pre_sum[-1] + num )% k)
            if pre_sum[-1] not in hash_map:
                hash_map[pre_sum[-1]] = i
            elif i - hash_map[pre_sum[-1]] > 1:
                return True

        return False