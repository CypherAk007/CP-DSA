# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=headA
        l2=headB
        # use dict store l1 address values and itrate l2 and find it in d if present return true
        d={}
        while(l1):
            d[l1]=l1.val
            l1=l1.next
        # print(d)
        while(l2):
            if l2 in d:
                return l2
            l2=l2.next
        return None
            