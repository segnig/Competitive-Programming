# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)


        for a, b in adjacentPairs:
            graph[b].append(a)
            graph[a].append(b)

        result = []

        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                result = [node, neighbors[0]]
                break
        
        
        while len(result) <= len(adjacentPairs):
            last, prev = result[-1], result[-2]
            candicates = graph[last]
            next = candicates[0] if candicates[0] != prev else candicates[1]
            result.append(next)

        return result