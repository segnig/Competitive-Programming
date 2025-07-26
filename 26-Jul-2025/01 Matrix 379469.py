# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(mat[0]) for _ in range(len(mat))]

        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        far = 1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    xx, yy = x + dx, y + dy
                    if self.inbound(mat, xx, yy) and result[xx][yy] == 0 and mat[xx][yy]==1:
                        queue.append((xx, yy))
                        result[xx][yy] = far
                
            far += 1
        return result

    def inbound(self, mat, x, y):
        return 0 <= x < len(mat) and 0 <= y < len(mat[0])