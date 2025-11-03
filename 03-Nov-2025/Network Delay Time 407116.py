# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for s, t, w in times:
            graph[s].append((t, w))

        queue = [(0, k)]

        visited = set([k])
        result = -1
        while queue and len(visited) < n:
            weight, node = heappop(queue)
            visited.add(node)
            result = max(result, weight)
            for nb, w in graph[node]:
                if nb not in visited:
                    heappush(queue, (w + weight, nb))
                    

        if len(visited) == n:
            return result
        return -1