# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []
        equal_to_pivot = []

        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                greater_than_pivot.append(num)
            else:
                equal_to_pivot.append(num)
        return less_than_pivot + equal_to_pivot + greater_than_pivot
        