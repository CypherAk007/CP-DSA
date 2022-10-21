# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1->create dummy node
        dummy=ListNode(0,head)
        
        # create a ptr before every start node of k grp 
        # so that after rev of the grp we can pt the 
        # prev node to kth node
        # 1(groupPrev)->2(k=1)->3(k=2) for k=2
        # after rev,
        # 1(groupPrev)->3->2 
        groupPrev=dummy
        
        
        while True:
            # get kth node 
            kth=self.getkth(groupPrev,k)
            # if there is no kth group
            if not kth:
                break
                
            # ptr after the kth group
            groupNext=kth.next
            
            # reverse the group
            prev=kth.next #insted of null
            curr=groupPrev.next
            while curr!=groupNext:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt 
            
            # 1(gp)->2->3(kth)->4(gnext)
            # 1->3(kth)->2->4
            temp=groupPrev.next #(stores 1st node in the grp)
            groupPrev.next=kth #1->3(kth)
            # now for future k rev we shift grpprev to start ofk grp
            # 1(gp)->3->2->4->5->
            # 1->3->2(gp)->4->5(newkth)->
            groupPrev=temp #the first node of prev grp
            
        return dummy.next
            
                
            
                
    def getkth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
    