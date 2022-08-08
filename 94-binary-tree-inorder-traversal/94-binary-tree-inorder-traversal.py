# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # l Rt r - Morris Traversal
        inorder=[]
        cur=root
        while(cur!=None):
            # case1->if no left
            if cur.left==None:
                inorder.append(cur.val)
                cur=cur.right
            # case2-> if left exist visit the last guy of left subtree
            else:
                # goto left
                prev=cur.left
                # now goto right most if exist and not pointing to cur
                while(prev.right and prev.right!=cur):
                    prev=prev.right
                # c-1->if prev.right is null make thread point to cur
                if prev.right==None:
                    prev.right=cur
                    # After making thread start traversal
                    cur=cur.left
                else:#C2-> if prev.right is pointing to cur
                    # remove the thread and make cur goto right
                    prev.right=None
                    # print the root val
                    inorder.append(cur.val)
                    cur=cur.right
                    
        return inorder
        
        
        