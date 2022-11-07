#User function Template for python3

class Solution:
    def countSquares(self, N):
        # code here 
        return self.bs(N)
    def bs(self,N):
        lo=1
        hi=N
        res=0
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if mid*mid>=N:
                hi=mid-1
            else:
                res=mid
                lo=mid+1 
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends