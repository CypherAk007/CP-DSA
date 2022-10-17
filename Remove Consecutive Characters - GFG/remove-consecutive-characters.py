#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        # return self.helper(S,0)
        return self.itr2helper(S)
    def helper(self,s,idx):
        # bc
        if idx==len(s):
            return ''
        
        if idx>0 and s[idx]==s[idx-1]:
            return self.helper(s,idx+1)
        else:
            res=self.helper(s,idx+1)
            res=s[idx]+res
            return res 
    def itrhelper(self,s):
        i=0
        s+='#'
        res=''
        while(s[i]!='#'):
            if s[i]!=s[i+1]:
                res+=s[i]
                i+=1 
            if s[i+1] and s[i]==s[i+1]:
                while(s[i+1]!='#' and s[i]==s[i+1]):
                    i+=1
        return res
    
    def itr2helper(self,s):
        n=len(s)
        res=""
        for i in range(n):
            if i<n-1 and s[i]==s[i+1]:
                continue
            else:
                # this satisify if last-1 char==lastchar or not equal
                # we have to store the last char
                res+=s[i]
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends