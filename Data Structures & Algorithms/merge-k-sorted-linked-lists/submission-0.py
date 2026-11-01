# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class heapObj:
    def __init__(self, val, ptr):
        self.val = val
        self.ptr = ptr
    
    def __lt__(self, other):
        return self.val < other.val


from heapq import heapify, heappush, heappop
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        ans_ptr = ListNode()
        for head in lists:
            if head:
                heappush(min_heap, heapObj(head.val, head))
        
        itr = ans_ptr
        while min_heap:
            top = heappop(min_heap).ptr
            itr.next = top
            itr = top
            if top.next:
                heappush(min_heap, heapObj(top.next.val, top.next))
        
        return ans_ptr.next


        