# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        in_degree = [0] * n
        graph = [[] for _ in range(n)]
        ancestors = [set() for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
                
        while q:
            u = q.popleft()
            for v in graph[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        return [sorted(ancestors[i]) for i in range(n)]