#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
def merge(a,b):
    temp=res=Node(0)
    while(a and b):
        if a.data<b.data:
            temp.bottom=a
            temp=temp.bottom
            a=a.bottom
        else:
            temp.bottom = b
            temp=temp.bottom 
            b=b.bottom 
    temp.bottom=a or b
    return res.bottom
    
def flatten(root):
    #Your code here
    if root==None or root.next==None: # (given root is None or we have reached the last node)
        return root
    
    # we go fm left to right till end and while returning 
    # we make the merge function
    
    root.next=flatten(root.next)
    
    # now merge present bottom to root.next bottom
    root = merge(root,root.next)
    
    # This will be merged with its left 
    return root
    

            
    
            
            
            
            
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag == 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 == 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends