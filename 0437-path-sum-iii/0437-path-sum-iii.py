# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.pathsum = collections.defaultdict(int)
        self.pathsum[0] = 1

        def dfs(r, cursum):
            if r is None:
                return

            cursum += r.val
            self.paths += self.pathsum[cursum - targetSum]
            self.pathsum[cursum] += 1

            if r.right:
                dfs(r.right, cursum)

            if r.left:
                dfs(r.left, cursum)

            self.pathsum[cursum] -= 1

        dfs(root, 0)
        return self.paths