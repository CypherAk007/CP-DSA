class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=m-1
        while(i>=0 and i<n and j>=0 and j<m):
            if matrix[i][j]==t:
                return True 
            elif matrix[i][j]>t:
                j-=1
            elif matrix[i][j]<t:
                i+=1 
        return False