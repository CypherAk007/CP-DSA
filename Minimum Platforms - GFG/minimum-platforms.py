#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        #  sort both in asc order
        arr.sort()
        dep.sort()
        platform=1 
        maxi=1
        i=1 #1st(0th) train is in platform
        j=0
        while(i<n and j<n):
        # if train has arrived before other train has left
            if arr[i]<=dep[j]: 
                platform+=1 
                i+=1
            # train leaves before another train arrives
            elif arr[i]>dep[j]:
                platform-=1 
                j+=1 
            
            if platform>maxi:
                maxi=platform
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends