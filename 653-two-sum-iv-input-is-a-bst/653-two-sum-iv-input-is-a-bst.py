# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Brutefroce convert to inorder and apply 2ptr
        lst=self.inorder(root)
        i=0
        j=len(lst)-1
        while i<j:
            if lst[i]+lst[j]==k:
                return True
            if k<lst[i]+lst[j]:
                j-=1
            else:
                i+=1
        return False
            
    def inorder(self,root):
        if root==None:
            return []
        lst=[]
        lst+=self.inorder(root.left)
        lst.append(root.val)
        lst+=self.inorder(root.right)
        return lst