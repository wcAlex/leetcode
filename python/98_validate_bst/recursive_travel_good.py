import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isValid(node: TreeNode, low=-math.inf, high=math.inf) -> bool:
            if node is None:
                return True
            
            if node.val >= high or node.val <= low:
                return False
            
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
            
        return isValid(root)

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
        
#         def validate(node, low=-math.inf, high=math.inf):
#             # Empty trees are valid BSTs.
#             if not node:
#                 return True
#             # The current node's value must be between low and high.
#             if node.val <= low or node.val >= high:
#                 return False
            
#             # The left and right subtree must also be valid.
#             return (validate(node.right, node.val, high) and
#                    validate(node.left, low, node.val))
        
#         return validate(root)