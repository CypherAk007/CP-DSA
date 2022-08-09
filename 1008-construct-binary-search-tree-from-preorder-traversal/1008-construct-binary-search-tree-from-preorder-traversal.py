# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder,float('inf'),[0])
    def helper(self,preorder,bound,i):
        if i[0]==len(preorder) or preorder[i[0]]>bound:#if index i out of range or val > bound
            return None
        root=TreeNode(preorder[i[0]])
        i[0]+=1
        root.left=self.helper(preorder,root.val,i)#if we are moving towards left then ub=curval
        root.right=self.helper(preorder,bound,i)#if right then prevnode ub carrys onn
        return root