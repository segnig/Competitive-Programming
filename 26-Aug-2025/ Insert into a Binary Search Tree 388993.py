# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        node = root
        self.insert(root, val)
        return root
    def insert(self, node, val):
        if node.val > val:
            if not node.left:
                node.left = TreeNode(val=val)
                return
            return self.insert(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(val=val)
                return
            return self.insert(node.right, val)