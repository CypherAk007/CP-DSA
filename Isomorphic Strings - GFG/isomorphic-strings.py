#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s,t):
        if len(s)!=len(t):
            return False
        mapST, mapTS={},{}
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if ((c1 in mapST and mapST[c1]!=c2) or
               (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            mapST[c1]=c2 
            mapTS[c2]=c1 
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends