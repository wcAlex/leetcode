import unittest
from solution1 import Solution1

class TestSum(unittest.TestCase):

    def test_solution1_case1(self):
        sol = Solution1()

        res = sol.romanToInt("III")
        self.assertEqual(res, 3)

        res = sol.romanToInt("LVIII")
        self.assertEqual(res, 58)

        res = sol.romanToInt("MCMXCIV")
        self.assertEqual(res, 1994)

    def test_solution1_case1(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()