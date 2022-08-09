# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=self.inorder(root)
        return a[k-1]
    def inorder(self,root):
        if root==None:
            return []
        lst=[]
        lst+=self.inorder(root.left)
        lst.append(root.val)
        lst+=self.inorder(root.right)
        return lst
    