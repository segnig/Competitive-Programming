# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        for i in range(len(strs[0])):

            prev_char = strs[0][i]

            for j in range(len(strs)):
                if strs[j][i] < prev_char:
                    count += 1
                    break
                prev_char = strs[j][i]

        return count