# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(node):
            itr = node
            prev = None
            while itr:
                tmp = itr.next
                itr.next = prev
                prev = itr
                itr = tmp
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        car = 0
        i1, i2 = l1, l2
        l3 = ListNode()
        i3 = prev = l3
        while i1 and i2:
            val = i1.val + i2.val + car
            car, val = val//10, val%10
            i3 = ListNode(val)
            prev.next = i3
            prev = i3
            i1, i2 = i1.next, i2.next
        while i1:
            val = i1.val + car
            car, val = val//10, val%10
            i3 = ListNode(val)
            prev.next = i3
            prev = i3
            i1 = i1.next
        while i2:
            val = i2.val + car
            car, val = val//10, val%10
            i3 = ListNode(val)
            prev.next = i3
            prev = i3
            i2 = i2.next
        if car:
            i3 = ListNode(car)
            prev.next = i3
        return reverseList(l3.next)
        