# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

from heapq import *

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = list(range(1, 1001))
        heapify(self.heap)
        self.in_heap = set(self.heap)
        
    def popSmallest(self) -> int:
        num = heappop(self.heap)
        self.in_heap.remove(num)
        return num

    def addBack(self, num: int) -> None:
        
        if num not in self.in_heap:
            heappush(self.heap, num)
            self.in_heap.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)