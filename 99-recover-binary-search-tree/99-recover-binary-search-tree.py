# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first=None
        self.prev=TreeNode(float('-inf'))
        self.middle=None
        self.last=None
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        if self.first and self.last: #if they are non adjecent
            self.first.val,self.last.val=self.last.val,self.first.val
        elif self.first and self.middle:
            self.first.val,self.middle.val=self.middle.val,self.first.val
            
    def inorder(self,root):
        if root==None:
            return 
        
        self.inorder(root.left)
        
        if self.prev!=None and (root.val<self.prev.val):
            # if this is first violation,mark these two nodes as 
            # first and middle
            if self.first==None:
                self.first=self.prev
                self.middle=root
            else:
                self.last=root
                
        # mark this node as previous
        self.prev=root
        
        self.inorder(root.right)
        
    