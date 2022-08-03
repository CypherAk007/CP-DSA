# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        
        cur=dummy
        nex=dummy
        pre=dummy
        
        # calc the len of ll
        count=0 
        while(cur.next!=None):
            cur=cur.next
            count+=1
        print(count)
        while(count>=k): #1st grp->c=8>3, 2nd grp->c=5>3,3rd grp c=2<3 stop oly 2 grp we itrate
            cur=pre.next#always cur points to the first node of a grp and pre is prev node to it.
            nex=cur.next#always nex points to the next node of cur.
            for i in range(1,k):#we have to reverse k-1 links
                cur.next=nex.next
                nex.next=pre.next
                pre.next = nex
                nex=cur.next
            pre=cur
            count-=k
        return dummy.next
            
        