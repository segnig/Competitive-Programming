# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        cols = len(mat[0])
        rows = len(mat) 
        pre_mat = [[0] * (cols + 1) for k in range(rows +1)]

        for row in range(1, len (pre_mat)):
            for col in range(1, len (pre_mat[0])):
                pre_mat[row][col] = mat[row-1][col-1] +  pre_mat[row][col - 1] +  pre_mat[row - 1][col] -  pre_mat[row - 1][col - 1]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                c1, r1 = max(0, c - k), max(0, r - k)
                c2, r2 = min(col - 1, c + k), min(rows - 1, r + k)

                r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
                mat[r][c] = (
                    pre_mat[r2][c2]
                    - pre_mat[r1 - 1][c2]
                    - pre_mat[r2][c1 - 1]
                    + pre_mat[r1 - 1][c1 - 1]
                )

        return mat  