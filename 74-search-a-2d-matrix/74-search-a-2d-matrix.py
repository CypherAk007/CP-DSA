class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=(n*m)-1
        # matrix[i][j] i=mid//no.col ; j=mid%no.col
        while low<=high:
            mid=(low+high)//2
            if target>matrix[mid//m][mid%m]:
                low=mid+1
            elif matrix[mid//m][mid%m]>target:
                high=mid-1
            else:
                return True
        return False