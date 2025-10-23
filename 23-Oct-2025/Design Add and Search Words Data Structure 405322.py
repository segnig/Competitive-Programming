# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current.child[index] is None:
                current.child[index] = Trie()
            current = current.child[index]
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end if node else False
            
            if node is None:
                return False
            
            char = word[index]
            
            if char == ".":
                for child in node.child:
                    if child is not None and dfs(index + 1, child):
                        return True
                return False
            else:
                child_index = ord(char) - ord("a")
                if node.child[child_index] is None:
                    return False
                return dfs(index + 1, node.child[child_index])
        
        return dfs(0, self.root)
            



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)