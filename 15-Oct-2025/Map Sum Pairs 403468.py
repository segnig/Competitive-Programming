# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class Trie:
    def __init__(self):
        self.c = [None for _ in range(26)]
        self.total = 0

class MapSum:

    def __init__(self):
        self.root = Trie()
        self.store = {}
        
    def insert(self, key: str, val: int) -> None:
        current = self.root
        red = self.store.get(key, 0)
        self.store[key] = val

        for char in key:
            ind = ord(char) - ord("a")

            if not current.c[ind]:
                current.c[ind] = Trie()
            current.c[ind].total += val - red
            current = current.c[ind]

        
    def sum(self, prefix: str) -> int:
        current = self.root
        

        for char in prefix:
            ind = ord(char) - ord("a")
            result = current.total
            current = current.c[ind]
            if not current:
                return 0

        return current.total

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)