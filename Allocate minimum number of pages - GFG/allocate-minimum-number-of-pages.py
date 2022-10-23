class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if N<M:
            return -1
            
        start=max(A)
        end=sum(A)
        res=-1
        while(start<=end):
            mid=start+(end-start)//2
            if self.isValid(A,N,mid,M)==True:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
    
    def isValid(self,A,N,mid,M):
        student=1
        summ=0
        for i in range(N):
            summ+=A[i]
            if summ>mid:
                student+=1 
                summ=A[i]
            if student>M:
                return False
        return True
        
            
            
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends