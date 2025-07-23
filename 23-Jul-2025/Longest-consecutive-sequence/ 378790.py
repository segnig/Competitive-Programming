# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class UnionFind:
    def __init__(self, nums):
        self.parent = {num:num for num in nums}
        self.size = {num:1 for num in nums}

    def find(self, x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return x

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if self.parent[root_v] == self.parent[root_u]:
            return 
        
        if self.size[root_v] > self.size[root_u]:
            self.parent[root_u] = self.parent[root_v]
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = self.parent[root_u]
            self.size[root_u] += self.size[root_v]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)

        for num in nums:
            if num + 1 in uf.parent:
                uf.union(num + 1, num)
            if num - 1 in uf.parent:
                uf.union(num - 1, num)
        result = 0
        if nums:
            result = max([m for _,  m in uf.size.items()])

        return result