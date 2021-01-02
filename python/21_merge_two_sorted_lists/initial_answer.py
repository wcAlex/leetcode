class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curNode = head
        while l1  and l2:
            if l1.val <= l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            
            curNode = curNode.next
            
        curNode.next = l1 or l2
        
        return head.next

