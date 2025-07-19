# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        target = counter[deck[0]]

        for _, num in counter.items():
            target = math.gcd(target, num)
        
        return target > 1