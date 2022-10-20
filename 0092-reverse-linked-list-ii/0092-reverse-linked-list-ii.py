# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1->2->3->4->5
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1->make a dummy head
        dummy = ListNode(0,head)
        
        # 2->move lp left prev to before left and curr to left
        # init
        leftPrev=dummy
        cur=head
        
        for i in range(left-1):
            leftPrev=cur
            cur=cur.next
        
        #3-> reverse from left to right -(r-l+1)
        prev=None
        for i in range(right-left+1):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        # 4-> link last node of revll->2 to curr->5
        # and also lp->1 to prev->4
        leftPrev.next.next=cur #cur node after right
        leftPrev.next=prev #prev=right
        
        return dummy.next
        
        
        
            
            