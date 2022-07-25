class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
                print(stack)
            else:
                if len(s)>0 and stack[-1]=='(' and s[i]== ')':stack.pop()

                elif len(s)>0 and stack[-1]=='[' and s[i]== ']':stack.pop()
                    
                elif len(s)>0 and stack[-1]=='{' and s[i]== '}':stack.pop()
                    
                else:
                    stack.append(s[i])
                    
            
        
        if len(stack)==0:
            return True
        else:
            return False