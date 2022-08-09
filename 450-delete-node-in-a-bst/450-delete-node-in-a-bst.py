# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        if root.val==key:
            return self.helper(root)
        dummy=root
        while(root!=None):
            if root.val>key:
                if root.left!=None and root.left.val==key:
                    root.left=self.helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right!=None and root.right.val==key:
                    root.right=self.helper(root.right)
                    break
                else:
                    root=root.right
        return dummy
    
    def helper(self,root):
        if root.left==None:
            return root.right 
        elif root.right==None:
            return root.left 
        rightChild=root.right
        lastRight=self.findLRight(root.left)
        lastRight.right=rightChild
        return root.left
    
    def findLRight(self,root):
        if root.right==None:
            return root
        return self.findLRight(root.right)
        