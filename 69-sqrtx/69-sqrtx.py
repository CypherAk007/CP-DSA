class Solution:
    def mySqrt(self, x: int) -> int:
        # return self.linear(x)
        return self.bs(x)
    def linear(self,x):
        # sqrt(x)>=y 
        # x>=y*y
        # tc-we go 0,1,2...,sqrt(x) ->O(sqrt(x))
        y=0
        while(y*y<=x):
            y+=1
        return y-1
    
    def bs(self,x):
        s=0
        e=x
        ans=0
        while(s<=e):
            m=s+(e-s)//2
            if m*m<=x:
                ans=m
                s=m+1
            else:
                e=m-1
        return ans