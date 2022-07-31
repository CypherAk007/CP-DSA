# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #  Rt l r - Itrative
        preorder=[]
        if root==None:
            return preorder
        s=[]
        s.append(root)
        while(len(s)!=0):
            root=s.pop()
            preorder.append(root.val)
            if root.right !=None:
                s.append(root.right)
            if root.left!=None:
                s.append(root.left)
        return preorder
        
        