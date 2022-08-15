# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root,isReverse=True):
        self.s=[]
        self.reverse=isReverse
        self.pushAll(root)
        
    def next(self) -> int:
        tempNode=self.s.pop()
        if self.reverse==False:
            self.pushAll(tempNode.right)
        else:
            self.pushAll(tempNode.left)
        return tempNode.val

    def hasNext(self) -> bool:
        if len(self.s)!=0:
            return True
        else:
            return False
        
    def pushAll(self,root):
        while(root!=None):
            self.s.append(root)
            if self.reverse==True:
                root=root.right
            else:
                root=root.left
            
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root==None:
            return False
        # This is for next
        l=BSTIterator(root,False)
        # before
        r=BSTIterator(root,True)
        
        i=l.next()
        j=r.next() # ==r.before()
        
        while(i<j):
            if i+j==k:
                return True
            elif (i+j<k):
                i=l.next()
            else:
                j=r.next()
        return False
    