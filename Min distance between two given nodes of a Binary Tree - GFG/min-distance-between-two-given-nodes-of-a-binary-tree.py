#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self,root,a,b):
    
        #return: minimum distance between a and b in a tree with given root
        #code here
        ans=[-1]
        self.findNode(root,a,ans)
        par={}
        self.makeParent(root,par)
        return self.bfs(ans[0],b,par)
        

    def makeParent(self,root,d):
        q=[root]
        while(q):
            n=q.pop(0)
            if n.left:
                d[n.left]=n
                q.append(n.left)
            if n.right:
                d[n.right]=n
                q.append(n.right)
            
    def findNode(self,root,a,ans):
        if root==None:
            return 
        self.findNode(root.left,a,ans)
        if root.data==a:
            ans[0]=root
            return 
        self.findNode(root.right,a,ans)
        
    def bfs(self,root,b,par):
        vis={}
        q=[]
        q.append([root,0])
        vis[root]=True
        while(q):
            n=q.pop(0)
            rt=n[0]
            step=n[1]
            
            if rt.data==b:
                return step
                
            if rt.left and rt.left not in vis:
                q.append([rt.left,step+1])
                vis[rt.left]=True
            if rt.right and rt.right not in vis:
                q.append([rt.right,step+1])
                vis[rt.right]=True
            if par.get(rt)!=None and par[rt] not in vis:
                q.append([par[rt],step+1])
                vis[par[rt]]=True
                
        return -1
    
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends