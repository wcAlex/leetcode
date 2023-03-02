from solution1 import SolutionA
import unittest

class TestSum(unittest.TestCase):

    def test_solution1_case1(self):
        sol = SolutionA()

        res = sol.isValid("()")
        self.assertTrue(res)

        res = sol.isValid("()[]{}")
        self.assertTrue(res)

        res = sol.isValid("(]")
        self.assertFalse(res)

        res = sol.isValid("([)]")
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()