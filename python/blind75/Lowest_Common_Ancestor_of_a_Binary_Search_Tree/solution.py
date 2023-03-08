class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/1347857/c-java-python-iterate-in-bst-picture-explain-time-o-h-space-o-1/
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
            
    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        if root.val > p.val and root.val > q.val:
             return self.lowestCommonAncestor2(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
             return self.lowestCommonAncestor2(root.right, p, q)
        else:
            return root
        

    # Find ancestor in a common binary tree. 
    # Didn't fully utilize the BST feature
    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left_root = self.lowestCommonAncestor(root.left, p, q)
        right_root = self.lowestCommonAncestor(root.right, p, q)

        if left_root and right_root:
            return root         
        elif left_root:
            return left_root
        else: 
            return right_root