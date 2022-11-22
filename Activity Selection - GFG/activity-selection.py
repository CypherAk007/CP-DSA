#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        arr=[]
        for i in range(n):
            arr.append([start[i],end[i]]) 
        arr.sort(key= lambda x: x[1])
        # print(arr)
        prevstart=arr[0][0]
        prevend=arr[0][1]
        c=1
        for i in arr:
            s=i[0]
            e=i[1]
            if s>prevend:
                c+=1
                prevend=e
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends