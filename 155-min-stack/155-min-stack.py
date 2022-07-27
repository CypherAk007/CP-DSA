class MinStack:
# tc-O(1) , sc-O(n)
    def __init__(self):
        self.s=[]
        self.mini=float('inf')

    def push(self, val: int) -> None:
        if len(self.s)==0:
            self.mini=val
            self.s.append(val)
        else:
            if val<self.mini:
                self.s.append(2*val-self.mini)
                self.mini=val
            else:
                self.s.append(val)
            
    def pop(self) -> None:
        if len(self.s)==0:
            return
        val=self.s.pop()
        if val<self.mini: #check if its modified val or not
            #roll back the mini
            self.mini=2*self.mini-val
            
    def top(self) -> int:
        val=self.s[-1]
        if val<self.mini:
            # its modified val
            return self.mini
        else:
            return val#stack top

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()