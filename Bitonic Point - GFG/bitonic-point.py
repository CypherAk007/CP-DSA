#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
	    pidx=self.findPeak(arr,n)
	    if pidx==-1:
	        return -1
	    return arr[pidx]
        
	def findPeak(self,arr,n):
	    n=len(arr)
	    lo=0
	    hi=n-1
	    while(lo<=hi):
	        mid=lo+(hi-lo)//2
	        if mid>0 and mid<n-1:
	            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
	                return mid
                elif arr[mid+1]>arr[mid]:
                    lo=mid+1 
                else:
                    hi=mid-1
            elif mid==0:
                if arr[mid]>arr[mid+1]:
                    return mid
                else:
                    return mid+1
                    
            elif mid==n-1:
                if arr[mid]>arr[mid-1]:
                    return mid
                else:
                    return mid-1
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends