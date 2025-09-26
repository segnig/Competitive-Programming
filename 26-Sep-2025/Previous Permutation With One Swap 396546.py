# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        if i >= 0:
            greater = i + 1

            for j in range(greater + 1, len(arr)):
                if arr[greater] < arr[j] < arr[i]: 
                    greater = j
            arr[greater], arr[i] = arr[i], arr[greater]
        return arr
        