#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        res=[0,0] #[rep,miss]
        countarr=[0]*(n+1)
        for i in range(n):
            countarr[arr[i]]+=1
        # print(countarr)
        for i in range(1,n+1):
            if countarr[i]==0:
                res[1]=i
                # print(res)
            if countarr[i]>1:
                res[0]=i
                # print(res)
        return res  
                
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends