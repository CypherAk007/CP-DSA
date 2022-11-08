#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        dp=[-1]*(n)
        # return self.helper(a,n-1,dp)
        return self.tabhelper(a,n)
    
    def helper(self,a,n,dp):
        # bc
        if n==0:
            return a[0]
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
            
        np=0+self.helper(a,n-1,dp)
        # p=float('-inf')
        # if n-2>=0:
        p=a[n]+self.helper(a,n-2,dp)
        dp[n]=max(p,np)
        return dp[n]
        
    def tabhelper(self,a,n):
        dp=[0]*(n)
        # bc
        dp[0]=a[0]
        
        for i in range(1,n):
            np=0+dp[i-1]
            p=a[i]
            if i>0:
                p+=dp[i-2]
            dp[i]=max(p,np)
        return dp[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends