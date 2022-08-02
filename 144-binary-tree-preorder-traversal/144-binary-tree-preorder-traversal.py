# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # All in one code
        s=[]
        s.append([root,1])
        pre=[]
        inorder=[]
        post=[]
        if root ==None:return 
        
        while(len(s)!=0):
            it = s.pop()
            # this is part of pre
            # we inc 1 to 2
            # pushthe left side of the tree
            if (it[1]==1):
                pre.append(it[0].val)
                it[1]+=1
                s.append(it)
                
                if it[0].left!=None:
                    s.append([it[0].left,1])
            # this is part of in
            # we inc 2 to 3
            # pushthe right side of the tree  
            elif (it[1]==2):
                inorder.append(it[0].val)
                it[1]+=1
                s.append(it)
                
                if it[0].right!=None:
                    s.append([it[0].right,1])
            # dont push it back again    
            else:
                
                post.append(it[0].val)
        return pre
        
        