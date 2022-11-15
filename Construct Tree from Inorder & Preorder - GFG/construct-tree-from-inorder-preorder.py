#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        inmap={}
        for i in range(n):
            inmap[inorder[i]]=i
        return self.helper(preorder,0,n-1,inorder,0,n-1,inmap)
    
    def helper(self,preorder,prestart,preend,inorder,instart,inend,inmap):
        if prestart>preend or instart>inend:
            return None
        root=Node(preorder[prestart])
        idx=inmap[root.data]
        numsleft=idx-instart
        root.left=self.helper(preorder,prestart+1,prestart+numsleft,inorder,instart,idx-1,inmap)
        root.right=self.helper(preorder,prestart+numsleft+1,preend,inorder,idx+1,inend,inmap)
        return root



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends