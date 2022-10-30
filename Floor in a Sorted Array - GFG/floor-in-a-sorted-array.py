class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        lo=0
        hi=N-1
        res=-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if A[mid]==X:
                res=mid
                return res
            if X<A[mid]:
                hi=mid-1
            else:
                res=mid
                lo=mid+1 
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends