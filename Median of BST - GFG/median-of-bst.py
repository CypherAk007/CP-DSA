#User function Template for python3

def findMedian(root):
    # code here
    # return the median
    count=[0]
    findLength(root,count)
    k=0
    out=[0,0]
    inorder(root,count[0]//2,0,out)
    if count[0]%2==0:
        x=out[0]+out[1]
        if x%2==0:
            return x//2
        else:
            return x/2
    else:
        return out[1]
        
def findLength(root,count):
    if root==None:
        return 
    findLength(root.left,count)
    count[0]+=1 
    findLength(root.right,count)
    

def inorder(root,k,c,out):
    s=[]
    cur=root
    while True:
        if cur:
            s.append(cur)
            cur=cur.left
        else:
            if len(s)==0:
                break
            cur=s.pop()
            c+=1
            if c==k:
                out[0]=cur.data
            if c==k+1:
                out[1]=cur.data
            cur=cur.right
    return-1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(findMedian(root))

# } Driver Code Ends