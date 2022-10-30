#User function Template for python3
class Solution:
    def solve(self, n, k, a):
        # Code here
        a.sort()
        lo=1 #min dist b/w two cows is atlest one
        hi=a[n-1]-a[0]
        res=0
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if self.canPlace(a,n,k,mid):
                res=mid
                lo=mid+1
            else:
                hi=mid-1
        return res
    
    def canPlace(self,a,n,cows,dist):
        cord=a[0]#first cow is placed
        cnt=1
        for i in range(1,n):
            if a[i]-cord>=dist:
                cnt+=1
                cord=a[i]
            if cnt==cows:
                return True
        return False
        
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, k = list(map(int, input().split()))
        v = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, v)
        print(res)
# } Driver Code Ends