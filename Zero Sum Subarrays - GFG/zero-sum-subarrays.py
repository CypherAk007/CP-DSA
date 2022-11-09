#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        count=0
        k=0
        summ=0
        d={}
        d[0]=1
        for i in range(len(arr)):
            summ+=arr[i]
            if summ-k in d:
                count+=d[summ-k]
            if summ in d:
                d[summ]+=1
            else:
                d[summ]=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends