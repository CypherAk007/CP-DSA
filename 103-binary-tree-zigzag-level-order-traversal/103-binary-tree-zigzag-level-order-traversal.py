# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # leftToRight=not(leftToRight)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag=-1 
        q=[]
        q.append(root)
        res=[]
        while q:
            qlen=len(q)
            temp=[]
            for i in range(qlen):
                v=q.pop(0)
                if v:
                    temp.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
            if temp:
                if flag==-1:
                    res.append(temp)
                else:
                    res.append(list(reversed(temp)))
                flag=flag*-1
        return res 