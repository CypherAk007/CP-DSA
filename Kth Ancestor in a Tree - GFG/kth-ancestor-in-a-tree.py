#User function Template for python3

def kthAncestor(root,k, node):
    #code here
    par={}
    makeParent(root,par)
    nth=findNode(root,node)
    
    while(k>0):
        if par.get(nth)!=None:
            nth=par[nth]
            k-=1 
        else:
            return -1
    return nth.data
        

def makeParent(root,d):
    q=[root]
    while(q):
        n=q.pop(0)
        if n.left:
            d[n.left]=n
            q.append(n.left)
        if n.right:
            d[n.right]=n
            q.append(n.right)

def findNode(root,t):
    q=[root]
    while(q):
        n=q.pop(0)
        if n.data==t:
            return n
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return -1
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        k,node=[int(x) for x in input().split()]
        s = input()

        root = buildTree(s)
        print(kthAncestor(root,k,node))
# } Driver Code Ends