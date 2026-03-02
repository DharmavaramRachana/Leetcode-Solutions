# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.ans = None

        def dfs(node):
            if not node:
                return 

            left = dfs(node.left)
            right = dfs(node.right)
            cur = node == q or node == p

            if (left and right) or (cur and left) or (cur and right):
                self.ans = node
                return True
            return cur or left or right

        dfs(root)
        return self.ans
            