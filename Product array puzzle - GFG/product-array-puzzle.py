#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        res=[1]*n
        
        prefix=1 
        for i in range(n):
            res[i]=prefix
            prefix=prefix*nums[i]
        
        postfix=1
        for i in range(n-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends