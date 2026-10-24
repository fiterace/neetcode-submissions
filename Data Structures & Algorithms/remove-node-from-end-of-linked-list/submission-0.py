# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        i = head
        while i:
            i = i.next
            sz += 1
        st = sz - n
        if not st:
            return head.next
        i = head
        st -= 1
        while st:
            i = i.next
            st -= 1
        i.next = i.next.next
        return head
        
        
        