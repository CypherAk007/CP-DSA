# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s=[]
        self.pushAll(root)
        
    def next(self) -> int:
        x=-1
        x=self.s.pop()
        self.pushAll(x.right)
        return x.val

    def hasNext(self) -> bool:
        if len(self.s)!=0:
            return True
        else:
            return False
        
    def pushAll(self,root):
        while(root!=None):
            self.s.append(root)
            root=root.left
            
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()