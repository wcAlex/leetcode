import unittest
from solution1 import Solution

class TestSum(unittest.TestCase):

    def test_solution1_case1(self):
        sol = Solution()

        res = sol.isPalindrome("A man, a plan, a canal: Panama")
        self.assertTrue(res)

        res = sol.isPalindrome("race a car")
        self.assertFalse(res)

        res = sol.isPalindrome("  ")
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()