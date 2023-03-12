import unittest
from solution import Solution, ListNode

class TestSum(unittest.TestCase):

    

    def test_solution1_case1(self):
        a, b, c, d = ListNode(), ListNode(), ListNode(), ListNode()
        a.val = 1
        a.next = b

        b.val = 2
        b.next = c

        c.val = 3
        c.next = d

        d.val = 4

        sol = Solution()
        res = sol.reverseList(a)
        print(res)

if __name__ == '__main__':
    unittest.main()