# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bruteForce
# inorder traversal keep a counter inplace of root.data
# tc-O(n)
# aux sc-o(h) h- logn as complete tree no skew tree

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        lh=self.getHeightLeft(root)
        rh=self.getHeightRight(root)
        
        if lh==rh:
            return int(math.pow(2,lh)-1)
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
    def getHeightLeft(self,root):
        count=0
        while(root!=None):
            count+=1
            root=root.left
        return count
    
    def getHeightRight(self,root):
        count=0
        while(root!=None):
            count+=1
            root=root.right
        return count
        