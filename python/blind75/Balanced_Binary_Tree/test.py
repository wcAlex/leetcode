from solution import Solution, TreeNode
import unittest

class TestSum(unittest.TestCase):

    def test_bs_case1(self):
        sol = Solution()

        node1 = TreeNode(val=1)
        node2 = TreeNode(val=2)
        node3 = TreeNode(val=2)
        node4 = TreeNode(val=3)
        node5 = TreeNode(val=3)
        node6 = TreeNode(val=4)
        node7 = TreeNode(val=4)

        node1.left = node2
        node1.right = node3

        node2.left = node4
        node2.right = node5

        node4.left = node6
        node4.right = node7

        res = sol.isBalanced(node1)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()