#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        # code here 
        if ((9*D)<S):
            return -1
        ans=""
        i=D-1
        while(i>=0):
            if S>9:
                ans='9'+ans
                S-=9
            else:
                if i==0: #8999
                    ans=str(S)+ans
                else:
                    ans=str(S-1)+ans
                    i-=1
                    while(i>0):
                        ans='0'+ans
                        i-=1
                    ans='1'+ans
                    break
            i-=1
        return ans
                    



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends