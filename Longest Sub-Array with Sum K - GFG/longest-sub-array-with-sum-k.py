#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        d={}
        d[0]=-1
        ans=0
        summ=0
        for i in range(N):
            summ+=A[i]
            if summ-K in d:
                length=i-d[summ-K]
                ans=max(ans,length)
            if summ not in d:
                d[summ]=i 
        return ans
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends