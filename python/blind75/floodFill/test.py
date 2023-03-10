from solution import Solution
import unittest

class TestSum(unittest.TestCase):

    def test_flood_case1(self):
        sol = Solution()

        res = sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
        print(res)
        self.assertEqual(res, [[2,2,2],[2,2,0],[2,0,1]])

        res = sol.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0)
        print(res)
        self.assertEqual(res, [[0,0,0],[0,0,0]])

if __name__ == '__main__':
    unittest.main()