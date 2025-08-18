# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {k: i for i, k in enumerate(arr2)}

        for num in arr1:
            if num not in order:
                order[num] = 10000000
        arr1.sort(key= lambda x : (order[x], x))

        return arr1