class Pair:
    def __init__(self):
        self.mx=float('-inf')
        self.mn=float('inf')
        
class Solution:
    def findSum(self,A,N): 
        #code here
        minmax=Pair()
        if N==1:
            return A[0]*2
        
        if A[0]>A[1]:
            minmax.max=A[0]
            minmax.min=A[1]
        else:
            minmax.min=A[0]
            minmax.max=A[1]
        
        for i in range(2,N):
            if A[i]>minmax.max:
                minmax.max=A[i]
            elif A[i]<minmax.min:
                minmax.min=A[i]
        return minmax.max+minmax.min



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends