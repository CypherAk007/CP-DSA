# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[-1]#as varibles are not passed by refference so we use arr of size 1.
        self.findheight(root,diameter)
        return diameter[0]
    def findheight(self,root,diameter):
        if root==None:
            return 0
        lh=self.findheight(root.left,diameter)
        rh=self.findheight(root.right,diameter)
        diameter[0]=max(diameter[0],lh+rh)
        return 1+max(lh,rh)