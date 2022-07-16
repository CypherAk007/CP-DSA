class Solution:
    def mySqrt(self, x: int) -> int:
        return self.linear(x)
    def linear(self,x):
        # sqrt(x)>=y 
        # x>=y*y
        # tc-we go 0,1,2...,sqrt(x) ->O(sqrt(x))
        y=0
        while(y*y<=x):
            y+=1
        return y-1