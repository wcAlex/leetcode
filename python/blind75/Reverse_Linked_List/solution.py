# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        root = ListNode()
        root.next = head
        while head and head.next:
            tmp = root.next
            root.next = head.next
            head.next = head.next.next
            root.next.next = tmp
        
        return root.next
    
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        while head:
            next = head.next 
            head.next = pre
            pre = head
            head = next

        return pre
            


        