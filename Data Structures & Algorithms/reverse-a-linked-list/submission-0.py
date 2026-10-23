# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        i = head
        prev = head
        i = i.next
        while(i):
            t = i.next
            i.next = prev
            prev = i
            i = t
        head.next = None
        return prev
