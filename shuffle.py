class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = nums[:n], nums[n:]
        result = []
        for i in range(n):
            result.append(left[i])
            result.append(right[i])

        return result
