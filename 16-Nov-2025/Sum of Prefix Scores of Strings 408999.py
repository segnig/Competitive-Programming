# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

class Solver:
    def __init__(self):
        self.root = Trie()
    
    def insert(self, word):
        current = self.root
        result = 0
        for index, char in enumerate(word):
            index = ord(char) - ord("a")
            if not current.children[index]:
                current.children[index] = Trie()
            current = current.children[index]
            current.count += 1
            result += current.count
    
        
    def count(self, word):
        current = self.root
        result = 0
        for index, char in enumerate(word):
            index = ord(char) - ord("a")
            current = current.children[index]
            result += current.count
    
        return result

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result = []

        solver = Solver()

        for word in words:
            solver.insert(word)

        for word in words:
            result.append(solver.count(word))

        return result