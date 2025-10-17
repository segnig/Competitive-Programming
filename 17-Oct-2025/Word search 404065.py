# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROW, COL = len(board), len(board[0])
        
        def inbound(row, col):
            return not (0 > col or col >= COL or 0 > row or row >=ROW)

        def dfs(row, col, i, visited=set()):
            if len(word) == i:
                return True
                
            if not inbound(row, col):
                return False
            
            if board[row][col] != word[i]:
                return False
            
            
            if (row, col) in visited:
                return False
            visited.add((row, col))

            for dr, dc in direction:
                nr, nc = dr + row, dc + col
                if dfs(nr, nc, i+1, visited):
                    return True
            
            visited.remove((row, col))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False