# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # M-1
        # we do preorder traversal simultaneously on both the trees
        # if p==None or q==None:
        #     return p==q
        # return (p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        
        # M-2 do preorder traversal and compare the returned arrays
        pTree=self.preorder(p)
        qTree=self.preorder(q)
        # print(pTree,qTree)
        return pTree==qTree
    def preorder(self,root):
        if root==None:
            return [None]
        lst=[]
        lst.append(root.val)
        lst+=self.preorder(root.left)
        lst+=self.preorder(root.right)
        return lst