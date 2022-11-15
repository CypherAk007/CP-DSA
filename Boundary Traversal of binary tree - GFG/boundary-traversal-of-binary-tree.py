#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        res=[]
        if self.checkleaf(root):
            return [root.data]
            
        if root==None:
            return res
        
        res.append(root.data)
        self.checkleft(root,res)
        self.addleaf(root,res)
        self.checkright(root,res)
        return res
        
    def checkleaf(self,root):
        # if root==None:
        #     return False
            
        if root.left==None and root.right==None:
            return True
        else:
            return False
    
    def checkleft(self,root,res):
        # temp=[]
        cur=root.left
        while(cur!=None):
            if self.checkleaf(cur)==False:
                res.append(cur.data)
            if cur.left!=None:
                cur=cur.left
            else:
                cur=cur.right
                
    def addleaf(self,root,res):
        # if root==None:
        #     return 
        if self.checkleaf(root)==True:
            res.append(root.data)
            return 
        if root.left!=None:
            self.addleaf(root.left,res)
        if root.right!=None:
            self.addleaf(root.right,res)
            
    def checkright(self,root,res):
        temp=[]
        cur=root.right
        while(cur!=None):
            if self.checkleaf(cur)==False:
                temp.append(cur.data)
            if cur.right!=None:
                cur=cur.right
            else:
                cur=cur.left
        
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends