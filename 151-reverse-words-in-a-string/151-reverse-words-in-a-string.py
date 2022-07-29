class Solution:
    def reverseWords(self, s: str) -> str:
        ans=''
        stack=[]
        temp=''
        for i in s:
            if i==' ':
                if temp!='':
                    stack.append(temp)
                temp=''
            else:
                temp+=i
        if temp!='':        
            stack.append(temp) 
            
        while(len(stack)!=1):
            x=stack.pop()
            ans+=x+" "
        ans+=stack.pop()
        return ans