# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        l = len(mat)
        for i in range(len(mat)):
            result += mat[i][i]
            result += mat[l-1-i][i]

        if l%2:
            result -= mat[l//2][l//2]

        return result