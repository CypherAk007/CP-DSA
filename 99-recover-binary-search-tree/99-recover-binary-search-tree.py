# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a=self.inorder(root)
        a.sort()
        i=[0]
        self.helper(root,a,i)
        
    def inorder(self,root):
        if root==None:
            return []
        lst=[]
        lst+=self.inorder(root.left)
        lst.append(root.val)
        lst+=self.inorder(root.right)
        return lst
    
    def helper(self,root,a,i):
        if root==None:
            return 
        self.helper(root.left,a,i)
        root.val=a[i[0]]
        i[0]+=1
        self.helper(root.right,a,i)
        