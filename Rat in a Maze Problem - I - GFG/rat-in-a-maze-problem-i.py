#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        
        vis=[[0]*n for i in range(n)]
        out=self.f(0,0,'',vis,m,n)
        if len(out)==0:
            return [-1]
        return out
        
    def f(self,r,c,p,vis,mat,n):
        # bc
        if r==n-1 and c==n-1:
            out=[]
            if mat[r][c]==1:
                out.append(p)
            return out
        
        if mat[r][c]==0:
            return []
        
        if vis[r][c]==1:
            return []
        
        vis[r][c]=1
        lst=[]
        if r>0:
            lst+=self.f(r-1,c,p+'U',vis,mat,n)
        
        if r<n-1:
            lst+=self.f(r+1,c,p+'D',vis,mat,n)
        
        if c>0:
            lst+=self.f(r,c-1,p+'L',vis,mat,n)
        
        if c<n-1:
            lst+=self.f(r,c+1,p+'R',vis,mat,n)
        
        vis[r][c]=0
        
        return lst
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends