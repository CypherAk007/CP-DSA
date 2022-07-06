# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return
        
        mid=self.findMiddle(head)
        hs=self.reverseList(mid)
        hf=head
        while(hf and hs):
            temp=hf.next
            hf.next=hs
            hf=temp
            temp=hs.next
            hs.next=hf
            hs=temp
            
        # Setting next of tail to null
        if hf!=None:
            hf.next=None
        
    # find Middle
    def findMiddle(self,head):
        s=head
        f=head
        while(f and f.next):
            s=s.next
            f=f.next.next
        return s
        
    # find reverse
    def reverseList(self,head):
        if head==None:
            return head
        p=None
        c=head
        n=c.next
        while(c):
            c.next=p
            p=c
            c=n
            if n!=None:
                n=n.next
        return p
        
        