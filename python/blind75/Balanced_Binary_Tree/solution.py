from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left_height = check(node.left)
            right_height = check(node.right)

            if left_height != -1 and right_height != -1 and abs(left_height - right_height) <= 1:
                return max(left_height, right_height) + 1
            else:
                return -1
            
        return check(root) != -1
