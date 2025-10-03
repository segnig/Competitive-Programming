# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        cups = [[0]* (query_row + 2) for _ in range(query_row + 2)]

        cups[1][1] = poured

        for row in range(2, query_row+2):
            for col in range(1, query_row+2):
                left = cups[row-1][col-1] - 1 if cups[row-1][col-1] > 1 else 0
                right = cups[row-1][col] - 1 if cups[row-1][col] > 1 else 0
                cups[row][col] = left / 2 + right / 2


        
        return cups[query_row+1][query_glass+1] if cups[query_row+1][query_glass+1] < 1 else 1