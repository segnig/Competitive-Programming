# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def bfs(node, total_sum):
            
            if not node.left and not node.right:
                return targetSum == total_sum + node.val
            
            result = False
            if node.left:
                result  = result or bfs(node.left, total_sum + node.val)
            if node.right:
                result  = result or bfs(node.right, total_sum + node.val)
                
            return result
        
        return bfs(root, 0)