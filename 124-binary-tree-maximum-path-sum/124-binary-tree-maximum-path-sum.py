# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxValue = [float('-inf')]
        self.maxPathDown(root,maxValue)
        return maxValue[0]
    
    def maxPathDown(self,node,maxValue):
        if node==None: return 0
        left=max(0,self.maxPathDown(node.left,maxValue))#ignores the -ve nodes
        right=max(0,self.maxPathDown(node.right,maxValue))#ignores the -ve nodes
        maxValue[0]=max(maxValue[0],left+right+node.val)
        #if heights of two paths are same then choose the higher sum path +curr nodeval
        return node.val+max(left,right)
        