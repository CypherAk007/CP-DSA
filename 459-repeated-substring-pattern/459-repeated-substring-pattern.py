class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l=len(s)
        for i in range(l//2,0,-1):
            if l%i==0:
                repeat=l//i
                substring=s[0:i]
                sb=''
                for j in range(0,repeat):
                    sb+=substring
                if sb==s:
                    return True
        return False
        