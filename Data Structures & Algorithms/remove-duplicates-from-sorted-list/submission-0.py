# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        prev = head
        if not i:
            return i
        i = i.next
        while(i != None):
            if i.val == prev.val:
                prev.next = i.next
            else:
                prev = prev.next
            i = i.next
        return head
        