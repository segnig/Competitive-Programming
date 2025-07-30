# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)

        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        
        count_even_level2, _ = self.bfs(tree2)

        even_count, even_level = self.bfs(tree1)
        answer = [len(edges1) - even_count + 1] * (len(edges1) + 1)

        for e in even_level:
            answer[e] = even_count
        
        for i in range(len(edges1) + 1):
            answer[i] += max(count_even_level2, len(edges2) - count_even_level2 + 1)
        
        return answer

    def bfs(self, tree):
        visited = set([0])
        level, count = 0, 0
        queue = deque([0])
        even_level_nodes = []

        while queue:
            if level % 2 == 0:
                count += len(queue)
                even_level_nodes.extend(list(queue))

            for _ in range(len(queue)):
                node = queue.popleft()
                for nb in tree[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            level += 1
        
        return count, even_level_nodes