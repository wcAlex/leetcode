import unittest
from solution import Solution1, ListNode

class TestSum(unittest.TestCase):

    def build_listnode(self, list: list) -> ListNode:
        head = ListNode()
        cur = head

        for v in list:
            n = ListNode()
            n.val = v
            cur.next = n
            cur = cur.next

        return head.next
    
    def check_equal(self, l: list, r: ListNode) -> bool:
        for v in l:
            if v != r.val:
                return False
            r = r.next
        
        return r == None

    def test_solution1_case1(self):
        sol = Solution1()

        res = sol.mergeTwoLists(list1 = self.build_listnode(list = [1,2,4]), list2 = self.build_listnode(list = [1,3,4]))
        self.assertTrue(self.check_equal([1,1,2,3,4,4], res))

if __name__ == '__main__':
    unittest.main()