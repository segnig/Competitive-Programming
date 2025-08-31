# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.cands = [[set(str(num) for num in range(1, 10)) for _ in range(9)] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.update_cands(board, i, j, board[i][j])
        
        self.solve(board)

    def solve(self, board):
        min_cands = 10
        best_cell = None
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' and len(self.cands[i][j]) < min_cands:
                    min_cands = len(self.cands[i][j])
                    best_cell = (i, j)
                    if min_cands == 1:
                        break
            if best_cell is not None and min_cands == 1:
                break

        if best_cell is None:
            return True
            
        
        i, j = best_cell
        for val in list(self.cands[i][j]):
            board[i][j] = val
            cands_copy = self.copy_cands()
            self.update_cands(board, i, j, val)
            
            if self.solve(board):
                return True
            
            board[i][j] = '.'
            self.restore_cands(cands_copy)
        
        return False

    def update_cands(self, board, i, j, val):
        for x in range(9):
            if val in self.cands[i][x]:
                self.cands[i][x].remove(val)
            if val in self.cands[x][j]:
                self.cands[x][j].remove(val)
        
        subgrid_row = (i // 3) * 3
        subgrid_col = (j // 3) * 3
        for x in range(subgrid_row, subgrid_row + 3):
            for y in range(subgrid_col, subgrid_col + 3):
                if val in self.cands[x][y]:
                    self.cands[x][y].remove(val)

    def copy_cands(self):
        return [[set(cell) for cell in row] for row in self.cands]

    def restore_cands(self, cands_copy):
        self.cands = cands_copy