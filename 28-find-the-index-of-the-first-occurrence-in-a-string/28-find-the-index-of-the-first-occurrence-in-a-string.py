class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP ALGO.
        if len(needle)==0:
            return 0
        # making of lps
        lps=[0]*len(needle)
        prevlps=0
        i=1
        while i<len(needle):
            if needle[i]==needle[prevlps]:
                lps[i]=prevlps + 1
                prevlps+=1
                i+=1
            else:
                if prevlps==0:
                    lps[i]=0
                    i+=1
                else:
                    prevlps=lps[prevlps-1]
        
        i=0
        j=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
            if j==len(needle):
                return i-len(needle)
        return -1