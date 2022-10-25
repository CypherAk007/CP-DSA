class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        lo=matrix[0][0]
        hi=matrix[n-1][m-1]
        while(lo<hi):
            mid=lo+(hi-lo)//2
            val=self.helper(matrix,n,m,mid)
            if val<k:
                lo=mid+1 
            else:
                hi=mid
        return hi
            
        
    def helper(self,matrix,n,m,t):
        i=0
        j=m-1
        c=0
        while(i<n and j>=0):
            if matrix[i][j]<=t:
                c+=j+1
                i+=1 
            else:
                j-=1
        return c
            
                 