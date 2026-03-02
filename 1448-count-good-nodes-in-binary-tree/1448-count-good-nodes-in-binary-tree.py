# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, n):
            if not node:
                return None

            if node.val >= n:
                n = node.val
                self.ans += 1

            dfs(node.left, n)
            dfs(node.right, n)

        dfs(root, root.val)
        return self.ans