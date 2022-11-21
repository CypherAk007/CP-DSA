# Your task is to complete this function
# function should return true/false or 1/0
def isdeadEnd(root):
    # Code here
    d1={} #leaf nodes
    d2={} #non leaf
    d2[0]=1
    inorder(root,d1,d2)
    # print(d1,d2)
    for i in d1:
        # print(i,i+1,i-1)
        if i+1 in d2 and i-1 in d2:
            return 1
    return 0

def inorder(root,d1,d2):
    if root==None:
        return None
    
    inorder(root.left,d1,d2)
    if checkLeaf(root):
        d1[root.data]=1
    else:
        d2[root.data]=1
    inorder(root.right,d1,d2)
    
def checkLeaf(root):
    if root.left==None and root.right==None:
        return True
    return False


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        if isdeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends