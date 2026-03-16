# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return True, 0  # An empty tree is balanced with height 0
            
            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)
            
            # Current node is balanced if left and right are balanced and height difference <= 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            # Height of current node
            height = 1 + max(left_height, right_height)
            
            return balanced, height
        
        result, _ = check(root)
        return result
        
        