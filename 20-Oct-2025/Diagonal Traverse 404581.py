# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        def traverse(row, col, direction):
            while 0 <= row < m and 0 <= col < n:
                result.append(mat[row][col])
                row += direction
                col -= direction
        
        for diag in range(m + n - 1):
            if diag % 2 == 0:
                if diag < m:
                    row, col = diag, 0
                else:
                    row, col = m - 1, diag - m + 1
                traverse(row, col, -1)
            else:
                if diag < n:
                    row, col = 0, diag
                else:
                    row, col = diag - n + 1, n - 1
                traverse(row, col, 1)
        
        return result