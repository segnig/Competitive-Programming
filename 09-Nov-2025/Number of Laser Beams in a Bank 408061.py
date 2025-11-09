# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        last = 0
        for row in bank:
            device = row.count("1")
            if device > 0:
                result += device * last
                last = device
        return result
        