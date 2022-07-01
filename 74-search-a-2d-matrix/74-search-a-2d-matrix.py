class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:        
        i=self.findRow(matrix,t,len(matrix[0]))
        # print(i)
        return self.binarySearch(matrix[i],0,len(matrix[0])-1,t)
    
    def findRow(self,matrix,t,last):
        for i in range(len(matrix)):
            if t<=matrix[i][last-1]:
                # print(i)
                return i
        return -1
            
    def binarySearch(self,a,l,h,t):
        # print(a,l,h,t)
        while(l<=h):
            m=(l+h)//2
            if t==a[m]:
                # print(m,a[m])
                return True
            elif t<a[m]:
                h=m-1
            else:
                l=m+1
        return False