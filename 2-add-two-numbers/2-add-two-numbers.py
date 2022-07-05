# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=l1
        s2=l2
        l3=s3=ListNode(0)
        print(s1.val,s2.val,s3.val)
        c=0
        while (s1 and s2):
            if s3.next==None:
                s3.next = ListNode()
            s3=s3.next
            ans=s1.val + s2.val+c
            s3.val = ans%10
            c=ans//10
            s1=s1.next
            s2=s2.next
        while(s1):
            if s3.next==None:
                s3.next = ListNode()
            s3=s3.next
            ans=s1.val+c
            s3.val = ans%10
            c=ans//10
            s1=s1.next
        while(s2):
            if s3.next==None:
                s3.next = ListNode()
            s3=s3.next
            ans=s2.val+c
            s3.val = ans%10
            c=ans//10
            s2=s2.next
        while(c):
            if s3.next==None:
                s3.next = ListNode()
            s3=s3.next
            ans=c
            s3.val = ans%10
            c=ans//10
            
        return l3.next