# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBst(root,float('-inf'),float('inf'))
    def isValidBst(self,root,minVal,maxVal):
        if root==None:
            return True
        if root.val>=maxVal or root.val<=minVal:
            return False
        return self.isValidBst(root.left,minVal,root.val) and self.isValidBst(root.right,root.val,maxVal)