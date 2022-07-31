# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # l Rt r
        if root==None:
            return []
        lst=[]
        lst+=self.inorderTraversal(root.left)
        lst.append(root.val)
        lst+=self.inorderTraversal(root.right)
        return lst
        