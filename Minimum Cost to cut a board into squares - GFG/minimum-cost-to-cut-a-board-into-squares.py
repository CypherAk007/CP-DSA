
from typing import List
class Solution:
    def minimumCostOfBreaking(self,X : List[int], Y : List[int],M : int, N : int) -> int:
        # code here
        m=M-1
        n=N-1 
        
        x=sorted(X,reverse=True)
        y=sorted(Y,reverse=True)
        hc=1 
        vc=1
        ans=0
        i=0
        j=0
        while(i<m and j<n):
            if x[i]>y[j]:
                ans+=x[i]*vc
                hc+=1
                i+=1
            else:
                ans+=y[j]*hc
                vc+=1
                j+=1
        while(i<m):
            ans+=x[i]*vc
            i+=1
        while(j<n):
            ans+=y[j]*hc
            j+=1
        return ans
            
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        m = a[0]
        n = a[1]
        
        tmp=IntArray().Input(a[0]-1) + IntArray().Input(a[1]-1)
        X = tmp[:m-1]
        Y = tmp[m-1:]
        
        obj = Solution()
        res = obj.minimumCostOfBreaking(X, Y,m,n)
        
        print(res)
        

# } Driver Code Ends