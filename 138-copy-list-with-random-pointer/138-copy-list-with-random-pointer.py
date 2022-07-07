"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# This code if finding on data so it wont work on [[3,null],[3,0],[3,null]]
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        itr=head
        front=head
        # s1->we make deep copy nodes aligned next to original nodes
        while(itr):
            front=itr.next
            copy=Node(itr.val)
            itr.next=copy
            copy.next=front
            itr=front
            
        # s2->we assign random ptr repectively to deep copy
        itr=head
        while(itr!=None):
            if itr.random!=None:
                itr.next.random = itr.random.next
            itr=itr.next.next
        
        # s3-> seprate original and deep copy
        itr=head
        front=None
        dummyHead=temp=Node(0)
        while(itr!=None):
            front=itr.next.next
            temp.next=itr.next
            itr.next=front
            itr=front
            temp=temp.next
        return dummyHead.next
            
        