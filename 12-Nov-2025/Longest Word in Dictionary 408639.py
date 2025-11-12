# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False


class Dictionary:
    def __init__(self):
        self.root = Trie()
        self.result = ""

    def insert(self, word):
        current = self.root
        valid = True
        
        for i, char in enumerate(word):
            index = ord(char) - ord("a")

            if not current.child[index]:
                current.child[index] = Trie()
            
            current = current.child[index]
            if i < len(word) - 1 and not current.is_end:
                valid = False
            
    
        current.is_end = True

        if valid:
             if len(word) > len(self.result) or (len(word) == len(self.result) and word < self.result):
                self.result = word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        dc = Dictionary()
        words.sort()
        words.sort(key=len)
        for word in words:
            dc.insert(word)
        return dc.result

