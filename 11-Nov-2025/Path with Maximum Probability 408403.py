# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)

        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((edge[1], prob))
            graph[edge[1]].append((edge[0], prob))
        
        queue = [(-1, start_node)]
        visited = defaultdict(int)

        while queue:
            prob, node = heappop(queue)
            prob = -prob
            if node == end_node:
                return prob
            
            for nb, prb in graph[node]:
                if prb * prob > visited[nb]:
                    heappush(queue, (- prb * prob, nb))

                    visited[nb] = prb * prob
           
        return 0