#User function Template for python3
import heapq
class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
    
    # Boolean comparator
    # compares the current.data and next.data in heap
    # so that we compare the data of the elements in the heap and 
    # not elements itself(i.e pointers)
    def __lt__(self, nxt):
        return self.data < nxt.data

class Solution:
    def huffmanCodes(self,S,f,N):
        # Code here
        heap=[]
        #1-> put all the ele in. heap
        for i in range(N):
            temp=Node(f[i])
            heapq.heappush(heap,temp)
            
        # 2-> pop min ele fm heap add make parent node store added val push
        while(len(heap)>1):
            left=heapq.heappop(heap)
            right=heapq.heappop(heap)
            newNode=Node(left.data+right.data)
            newNode.left=left 
            newNode.right=right
            heapq.heappush(heap,newNode)
            
        #  3-> only one ele is left in heap
        root=heapq.heappop(heap)
        ans=[]
        temp=''
        self.traverse(root,ans,temp) #do preorder traversal
        return ans
    
    def traverse(self,root,ans,temp):
        if root.left==None and root.right==None:
            ans.append(temp)
            return 
        
        self.traverse(root.left,ans,temp+'0')
        self.traverse(root.right,ans,temp+'1')

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S= input()
		N= len(S);
		f= [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.huffmanCodes(S,f,N)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends