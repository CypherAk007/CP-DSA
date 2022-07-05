# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def lengthCycle(self,head):
        fast=head
        slow=head
        length=0
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            # print(fast.val,slow.val)
            if fast==slow:
                temp=slow
                while True:
                    temp=temp.next
                    length+=1
                    if temp==slow:
                        break
                # print(length)
                return length
            
        return 0

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # Find the length of the cycle
            length =0
            fast=head
            slow=head

            while(fast!=None and fast.next!=None):
                fast=fast.next.next
                slow=slow.next
                if fast==slow:
                    length = self.lengthCycle(slow)
                    # print(length)
                    break

            if length==0:
                return None
            # Find the start node
            # print('in0')
            f=head
            s=head
            # print(f.val,s.val)
            # we have to move s by length(l) of the cycle times
            while(length>0):
                # print('in1')
                # print(s.val)
                s=s.next
                length-=1
            # we move both f(start to k) and s(l-(l-k)) till they meet at the start of the cycle
            while(f!=s):
                # print('in2')
                f=f.next
                s=s.next
                # print(f.val,s.val)

            return f