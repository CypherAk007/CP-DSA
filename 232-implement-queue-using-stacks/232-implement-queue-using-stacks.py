class MyQueue:

    def __init__(self):
        self.ip=[]
        self.op=[]

    def push(self, x: int) -> None:
        self.ip.append(x)

    def pop(self) -> int:
        if len(self.op)!=0:
            return self.op.pop()
        else:
            while(len(self.ip)!=0):
                val=self.ip.pop()
                self.op.append(val)
                
        return self.op.pop()

    def peek(self) -> int:
        if len(self.op)!=0:
            return self.op[-1]
        else:
            while(len(self.ip)!=0):
                val=self.ip.pop()
                self.op.append(val)
        return self.op[len(self.op)-1]
        

    def empty(self) -> bool:
        return True if len(self.ip)==0 and len(self.op)==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()