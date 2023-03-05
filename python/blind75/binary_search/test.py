from solution import Solution
import unittest

class TestSum(unittest.TestCase):

    def test_bs_case1(self):
        sol = Solution()

        res = sol.search(nums = [-1,0,3,5,9,12], target=13)
        self.assertEqual(res, -1)

        res = sol.search(nums = [-1,0,3,5,9,12], target=9)
        self.assertEqual(res, 4)

        res = sol.search(nums = [-1,0,3,5,9,12], target = 2)
        self.assertEqual(res, -1)

if __name__ == '__main__':
    unittest.main()