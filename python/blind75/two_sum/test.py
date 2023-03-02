from solution1 import SolutionA
import unittest

class TestSum(unittest.TestCase):

    def test_solution1_case1(self):
        sol = SolutionA()

        res = sol.twoSum(nums = [2,7,11,15], target = 9)
        print(res)
        self.assertEqual(res, [0,1])

        res = sol.twoSum(nums = [3,2,4], target = 6)
        print(res)
        self.assertEqual(res, [1,2])

        res = sol.twoSum(nums = [3,3], target = 6)
        print(res)
        self.assertEqual(res, [0,1])

if __name__ == '__main__':
    unittest.main()