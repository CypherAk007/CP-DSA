# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergeddLists=[]
            
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1) <len(lists) else None
                mergeddLists.append(self.mergeList(l1,l2))
            lists=mergeddLists
        return lists[0]
        
        
        
    def mergeList(self,l1,l2):
        dummy=ListNode(0)
        temp=dummy
        while(l1!=None and l2!=None):
            if l1.val<l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
            
        temp.next=l1 or l2
        return dummy.next
    
            
                