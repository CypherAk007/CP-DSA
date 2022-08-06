# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:#tc-o(n)sc-o(n) if skew
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root==p or root==q:#(None,None)fmboth sides or (7,None)or(None,3) 
            return root
        
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        
        if left==None:
            return right#even if right is None return
        elif (right==None):
            return left
        else:#if we get(7,3) from the lower calls we carry the current root val as output
            return root