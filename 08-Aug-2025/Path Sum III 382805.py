# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = defaultdict(int)
        result, running_sum, counter[0] = 0, 0, 1

        def dfs(root):
            nonlocal running_sum, result
            if not root:
                return result
            running_sum += root.val
            result += counter[running_sum - targetSum]
            counter[running_sum] += 1
            dfs(root.left)
            dfs(root.right)
            counter[running_sum] -= 1
            running_sum -= root.val
            
            return result
        
        return dfs(root)