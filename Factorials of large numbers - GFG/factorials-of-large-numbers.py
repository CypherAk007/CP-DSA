#User function Template for python3

class Solution:
    def factorial(self, n):
        res = []
        res.append(1)
        # print(res,res_size)
        x=2
        while x<=n:
            self.multiply(x,res,len(res))
            x+=1
        # print(res)
        res.reverse()
        s="".join(str(i) for i in res)
        # print(s)
        return s
        
                    
    def multiply(self,x,res,res_size):
        carry=0
        i=0
        while i<res_size:
            prod = res[i]*x+carry
            res[i]=prod%10
            carry=prod//10
            i+=1
        while(carry):
            res.append(carry%10)
            carry=carry//10

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends