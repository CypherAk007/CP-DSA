# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d={}
        ans=[]
        q=[]
        q.append((root,0,0))#root,vertical,level
        while(len(q)!=0):
            tup=q.pop(0)
            node=tup[0]
            x=tup[1]#vertical
            y=tup[2]#level
            
            if d.get(x)==None:
                d[x]={}
            
            if d[x].get(y)==None:
                d[x][y]=[]
            
            d[x][y].append(node.val)
            d[x][y].sort()
            if node.left!=None:
                q.append((node.left,x-1,y+1))
            if node.right!=None:
                q.append((node.right,x+1,y+1))
        # print(d)
        lst=[]
        for i in sorted(d):
            col=[]
            for j in d[i]:
                # print(i,j)
                # print(d[i].get(j))
                col+=d[i][j]
            ans.append(col)
        return ans
        
            
        