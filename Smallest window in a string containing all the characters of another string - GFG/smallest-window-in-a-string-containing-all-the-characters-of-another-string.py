#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, a, t):
        if len(t)>len(a):
            return -1
        d={}
        for i in range(len(t)):
            if t[i] not in d:
                d[t[i]]=1 
            else:
                d[t[i]]+=1
        # print(d)
        count=len(d)
        i=0
        j=0
        
        mini=float('inf')
        minstr=''
        while(j<len(a)):
            if a[j] in d:
                d[a[j]]-=1 
                if d[a[j]]==0:
                    count-=1
            
            if count>0:
                j+=1 
                
            if count==0:
                while(count==0):
                    if mini>(j-i+1):
                        mini=j-i+1
                        minstr=a[i:j+1]
                    # mini=min(mini,j-i+1)
                
                    if a[i] in d:
                        d[a[i]]+=1 
                        if d[a[i]]==1:
                            count+=1 
                    i+=1 
                j+=1
                    
                    # if count==0:
                    #     mini=min(mini,j-i+1)
                    
        if mini==float('inf'):
            return -1
        return minstr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends