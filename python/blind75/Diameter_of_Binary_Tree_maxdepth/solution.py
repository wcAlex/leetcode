from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return -1, 0 

            left_depth, left_diameter = dfs(node.left)
            right_depth, right_diameter = dfs(node.right)

            depth = 1 + max(left_depth, right_depth)
            diameter = max(left_depth + right_depth + 2, max(left_diameter, right_diameter))

            return depth, diameter

        return dfs(root)[1]
    
    # Use self.res as the external object, which make the program more
    # efficient
    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
    
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1 

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            depth = 1 + max(left_depth, right_depth)
            self.res = max(left_depth + right_depth + 2, self.res)

            return depth

        dfs(root)

        return self.res