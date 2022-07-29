class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        i=0
        j=0
        k=len(needle)
        while j<len(haystack):
            if j-i+1<k:
                j+=1
            elif j-i+1==len(needle):
                if haystack[i:j+1]==needle:
                    return i
                j+=1
                i+=1
        return -1