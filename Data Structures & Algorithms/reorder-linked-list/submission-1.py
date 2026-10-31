# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next # from here we reverse
        slow.next = None
        slow = temp

        prev = None
        while (slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        head2 = prev

        while (head2):
            tmp1 = head.next
            tmp2 = head2.next
            head.next = head2
            head2.next = tmp1
            head2 = tmp2
            head = tmp1