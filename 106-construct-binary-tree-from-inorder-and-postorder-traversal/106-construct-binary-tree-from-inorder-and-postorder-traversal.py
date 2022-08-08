# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #hash inorder values
        inmap={}
        for i in range(len(inorder)):
            inmap[inorder[i]]=i 
        # now we have twoptrs for inorder and postorder
        # prestart preend instart inend
        return self.cBtPreHelper(postorder,0,len(postorder)-1,
                                 inorder,0,len(inorder)-1,inmap)
    def cBtPreHelper(self,postorder,poststart,postend,inorder,instart,inend,inmap):
        # if array is empty
        if poststart>postend or instart>inend:
            return None
        
        root=TreeNode(postorder[postend])
        
        inRoot=inmap[root.val]#index of root in inorder
        numsLeft=inRoot-instart
        
        root.left=self.cBtPreHelper(postorder,poststart,poststart+numsLeft-1,
                                    inorder,instart,inRoot-1,inmap)
        root.right=self.cBtPreHelper(postorder,poststart+numsLeft,
                                    postend-1,inorder,inRoot+1,inend,inmap)
        
        return root
        