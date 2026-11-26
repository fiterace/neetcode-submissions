# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lena = 0
        lenb = 0
        ita = headA
        itb = headB
        while ita:
            ita = ita.next
            lena += 1
        while itb:
            itb = itb.next
            lenb += 1
        headA, headB = (headB, headA) if lena < lenb else (headA, headB)
        diff = abs(lena - lenb)
        ita = headA
        itb = headB
        while diff:
            ita = ita.next
            diff -= 1
        while ita and itb:
            if ita == itb:
                return ita
            ita, itb = ita.next, itb.next
        return None

        