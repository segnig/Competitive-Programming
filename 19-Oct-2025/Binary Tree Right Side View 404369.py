# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)
        def dfs(node, level):

            if not node:
                return 
            
            levels[level].append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        result = []
        dfs(root, 0)
        level = 0
        while  level in levels:
            result.append(levels[level][0])
            level += 1
        
        return result