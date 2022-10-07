class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        s=s+s
        # print(s)
        alt1=""
        alt2=""
        for i in range(len(s)):
            alt1+="0"if i%2 else "1"
            alt2+="1"if i%2 else "0"
        # print(alt1,alt2,len(alt1))
        res=float('inf')
        diff1,diff2=0,0
        i=0
        j=0
        # while(j<len(s)):
        for j in range(len(s)):
            if s[j]!=alt1[j]:
                diff1+=1
            if s[j]!=alt2[j]:
                diff2+=1 
            
            # if j-i+1<n:
            #     j+=1 
            
            if j-i+1>n:
                if s[i]!=alt1[i]:
                    diff1-=1
                if s[i]!=alt2[i]:
                    diff2-=1
                i+=1
                # j+=1
            
            if j-i+1==n:
                res=min(res,diff1,diff2)
                # j+=1 
        return res
                    