# Problem: Check if array is sorted - https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def isSorted(self, arr) -> bool:
        left = 0
        while left < len(arr) - 1:
            if arr[left] > arr[left + 1]:
                return False
            left += 1
        return True
                