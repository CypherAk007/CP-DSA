#User function Template for python3
from copy import copy
class Solution:
    def minSubset(self, A,N):
        A.sort()
        presum=A[:]
        suffsum=copy(A)
        for i in range(1,N):
            presum[i]=presum[i]+presum[i-1]
        
        for j in range(N-2,-1,-1):
            suffsum[j]=suffsum[j]+suffsum[j+1]
        
        i=N-2
        j=N-1
        while(i>=0 and j>=0):
            # print(suffsum[j],presum[i])
            if suffsum[j]>presum[i]:
                return N-j
            i-=1 
            j-=1
                
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSubset(A,N)
        print(ans)
# } Driver Code Ends