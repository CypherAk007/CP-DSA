class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        i=0
        j=m-1
        c=0
        while(j>=0 and j<m and i>=0 and i<n):
            # print(i,j,c)
            if j==0 and grid[i][j]<0:
                c+=m-(j)
                # print(c)
                i+=1
            elif grid[i][j]>=0:
                c+=m-(j+1)
                # print('c2',c,n,j+1)
                i+=1
            elif grid[i][j]<0:
                j-=1
            
        return c
