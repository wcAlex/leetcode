from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # post-order travel
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)

            tmp = root.left
            root.left = root.right
            root.right = tmp

        return root
    
    # pre-order travel
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)

        return root
    
    # BFS travel
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = deque([root])

        while len(tree):
            node = tree.pop()
            if not node:
                continue

            tmp = node.left
            node.left = node.right
            node.right = tmp

            tree.appendleft(node.left)
            tree.appendleft(node.right)
            
        return root
        