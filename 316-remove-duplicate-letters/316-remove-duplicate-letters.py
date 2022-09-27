class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # used to store the last index of every char in the s
        lastIndex=[-1]*26
        for i in range(0,len(s)):
            lastIndex[ord(s[i])-ord('a')]=i
        
        # visited array
        seen=[False]*26
        
        st=[] #stack
        
        for i in range(0,len(s)):
            c=ord(s[i])-ord('a') 
            
            if seen[c]==True:
                continue
            # if stack top is greater than incomming ele and stack top is not at its last index a<c(st.top)
            while(len(st)!=0 and st[-1]>c and i<lastIndex[st[-1]]):
                seen[st.pop()]=False
            st.append(c)
            seen[c]=True
  
        res=''
        for i in range(len(st)):
            res+=chr(st.pop()+ord('a'))
            
        # reverse the stack order
        res=res[::-1]
        return res
            
        