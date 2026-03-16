# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, cursum):
            if not node:
                return

            path.append(node.val)
            cursum += node.val

            if not node.left and not node.right and cursum == targetSum:
                res.append(path.copy())

            dfs(node.left, path, cursum)
            dfs(node.right, path, cursum)

            path.pop()

        dfs(root, [], 0)
        return res

            