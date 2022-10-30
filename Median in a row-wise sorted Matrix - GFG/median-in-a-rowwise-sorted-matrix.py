#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
    	#code here 
    	lo=float('inf')
    	hi=float('-inf')
    	for i in range(R):
    	    lo= min(lo,matrix[i][0])
    	    hi=max(hi,matrix[i][C-1])
    	while(lo<=hi):
    	    mid=lo+(hi-lo)//2
    	    cnt=0
    	    for i in range(R):
    	        cnt+=self.bsr(matrix[i],R,C,mid)
    	   # lessele=self.findSmallerEle(matrix,R,C,mid)
                	   
    	    if cnt<=((R*C)//2):
    	        lo=mid+1 
    	    else:
    	        hi=mid-1 
        return lo
    	
    
    def findSmallerEle(self,a,R,C,t): #ceil of target and gives no. of ele less than t inc. itself
        c=0
        for i in range(R):
            c+=self.bsr(a[i],R,C,t)
        return c
        
    def bsr(self,a,R,C,t):
        lo=0
        hi=C-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if a[mid]<=t:
                lo=mid+1 
            else:
                hi=mid-1 
        return lo 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends