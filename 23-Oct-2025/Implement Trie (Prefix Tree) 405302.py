# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.front = set()
        

    def insert(self, word: str) -> None:
        self.front.add(word)

    def search(self, word: str) -> bool:
        for _word in self.front:
            if _word == word:
                return True

        return False
        

    def startsWith(self, prefix: str) -> bool:
        for _word in self.front:
            if _word.startswith(prefix):
                return True

        return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)