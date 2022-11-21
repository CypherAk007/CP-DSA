#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def post_order(pre, size) -> Node:
    #code here
    return helper(pre,float('inf'),[0])

def helper(preorder,bound,i):
    if i[0]==len(preorder) or preorder[i[0]]>bound:
        return None
    root=Node(preorder[i[0]])
    i[0]+=1
    root.left = helper(preorder,root.data,i)
    root.right=helper(preorder,bound,i)
    return root
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=post_order(pre,size)

        postOrd(root)
        print()
# } Driver Code Ends