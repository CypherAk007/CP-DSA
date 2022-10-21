#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        # 1->check if arr is rotated or not
        if arr[0]<=arr[n-1]:
            return 0 
        
        # 2->find the index of min ele -> no.of rotations
        # find min ele with help of bs
        out=self.rotatedbs(arr,0,len(arr)-1,len(arr))
        return out
        
    def rotatedbs(self,arr,lo,hi,n):
        while(lo<=hi):
            mid=lo+(hi-lo//2)
            nxt=(mid+1)%n
            prev=(mid+n-1)%n
            # if mid <mid+1 and <mid-1 then its min ele
            if arr[mid]<=arr[nxt] and arr[mid]<=arr[prev]:
                return mid 
            elif arr[lo]<=arr[mid]:#left is sorted move right
                lo=mid+1
                # n=hi-lo+1
            elif arr[mid]<=arr[hi]:
                hi=mid-1
                # n=hi-lo+1
        return -1 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends