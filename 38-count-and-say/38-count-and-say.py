class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        if n==2:
            return '11'
        s='11'
        for i in range(3,n+1):
            t='' #stores the next iteration value
            s=s+'$'
            c=1
            for j in range(1,len(s)):
                if s[j]!=s[j-1]:
                    t=t+str(c)
                    t=t+s[j-1]
                    c=1
                else:
                    c+=1
            s=t
        return s
        