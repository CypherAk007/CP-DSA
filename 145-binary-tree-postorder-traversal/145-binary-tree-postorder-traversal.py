# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #  l r Rt - using two stacks
        s1=[]
        s2=[]
        postOrder=[]
        if root==None:
            return postOrder
        s1.append(root)
        while(len(s1)!=0):
            root=s1.pop()
            s2.append(root)
            if root.left!=None:
                s1.append(root.left)
            if root.right!=None:
                s1.append(root.right)
        while (len(s2)!=0):
            postOrder.append(s2.pop().val)
        return postOrder