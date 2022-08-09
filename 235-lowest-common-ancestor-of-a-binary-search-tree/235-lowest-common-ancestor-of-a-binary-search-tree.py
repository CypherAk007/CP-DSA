# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while(root!=None):
            cur=root.val
            if p.val>cur and q.val>cur:
                root=root.right
            elif p.val<cur and q.val<cur:
                root=root.left
            else:
                return root #if both are in diff dir or undecidible dir(root is p or q)