class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        while left<right and top<bottom:
            # get every i in top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            
            # get every ele in the rightmost col
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            
            # if we have[1,2,3] or [[1],[2],[3]] then we have to check and stop
            if not (left<right and top<bottom):
                break
            
            # get every ele in the bottom row
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            # get every ele in the left col
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            
        return res