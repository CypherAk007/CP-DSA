# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #  Rt l r
        if root==None:
            return []
        lst=[]
        lst.append(root.val)
        lst+=self.preorderTraversal(root.left)
        lst+=self.preorderTraversal(root.right)
        return lst
        