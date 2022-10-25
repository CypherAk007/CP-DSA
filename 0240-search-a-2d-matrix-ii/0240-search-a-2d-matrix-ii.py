class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        lo=0
        hi=m-1
        while(lo>=0 and lo<n and hi>=0 and hi<m):
            # mid=lo+(hi-lo)//2
            if matrix[lo][hi]==target:
                return True
            if target>matrix[lo][hi]:
                lo+=1
            elif target<matrix[lo][hi]:
                hi-=1
        return False