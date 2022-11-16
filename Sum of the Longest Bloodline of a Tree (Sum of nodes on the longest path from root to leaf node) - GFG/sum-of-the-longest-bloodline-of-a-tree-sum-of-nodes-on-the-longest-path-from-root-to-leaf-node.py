#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #code here
        ans=self.helper(root)
        # print(ans)
        return ans[1] #[height,sum]
        
    def helper(self,root):
        if root==None:
            return [0,0] #[height,sum]
        l=self.helper(root.left)
        r=self.helper(root.right)
        if l[0]>r[0]:
            return [l[0]+1,l[1]+root.data]
        if l[0]<r[0]:
            return [r[0]+1,r[1]+root.data]
        else:
            return [l[0]+1,max(l[1],r[1])+root.data]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.sumOfLongRootToLeafPath(root)
        print(res)
# } Driver Code Ends