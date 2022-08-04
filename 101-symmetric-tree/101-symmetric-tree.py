# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root==None or self.isSymHelper(root.left,root.right)
    def isSymHelper(self,left,right):
        if left==None or right==None:
            return left==right
        if left.val!=right.val:
            return False
        return self.isSymHelper(left.left,right.right) and self.isSymHelper(left.right,right.left)