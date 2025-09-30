# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(root):
            if not root:
                return 0
            
            take = root.val

            root_left = root.left
            root_right = root.right

            if root_right:
                take += dp(root_right.left)
                take += dp(root_right.right)
            if root_left:
                take += dp(root_left.left)
                take += dp(root_left.right)

            not_take = dp(root_right) + dp(root_left)

            return max(not_take, take)
        
        return dp(root)