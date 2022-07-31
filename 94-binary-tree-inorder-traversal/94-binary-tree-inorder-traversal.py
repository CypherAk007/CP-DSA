# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # l Rt r - itrative
        inorder=[]
        stack=[]
        node=root
        while(True):
            if node!=None:
                stack.append(node)
                node=node.left
            else:
                if len(stack)==0:
                    break
                node=stack.pop()
                inorder.append(node.val)
                node=node.right
        return inorder
        
        
        