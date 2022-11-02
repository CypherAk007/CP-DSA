#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        arr=[]
        for i in range(n):
            arr.append([start[i],end[i]])
        # print(arr)
        arr.sort(key = lambda x:x[1])
        # print(arr)
        ansst=arr[0][0]
        ansend=arr[0][1]
        c=1
        for i in arr:
            s=i[0]
            e=i[1]
            if s>ansend:
                c+=1 
                ansend=e 
        return c


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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends