# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        i = head
        n = 0
        arr = []
        while i:
            arr.append(i.val)
            i = i.next
            n += 1
        newa = reversed(arr)
        for i,j in zip(newa,arr):
            if i != j:
                return False
        return True