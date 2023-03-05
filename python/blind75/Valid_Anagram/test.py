import unittest
from solution import Solution

class TestAnagram(unittest.TestCase):

    def test_solution1_case1(self):
        sol = Solution()

        res = sol.isAnagram(s = "ab", t = "ba")
        self.assertTrue(res)    

        res = sol.isAnagram(s = "anagram", t = "nagaram")
        self.assertTrue(res)

        res = sol.isAnagram(s = "rat", t = "car")
        self.assertFalse(res)    

if __name__ == '__main__':
    unittest.main()