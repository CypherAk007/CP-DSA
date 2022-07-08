class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        out=""
        for i in range(len(s)):
            currentChar=s[i]
            if len(stack)>0 and stack[-1] == currentChar:
                stack.pop()
            else:
                stack.append(currentChar)
                
        for i in range(len(stack)):
            out+=stack[i]
        return out
                