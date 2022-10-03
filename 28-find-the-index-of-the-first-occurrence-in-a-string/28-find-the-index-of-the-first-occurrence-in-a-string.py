class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        i=0
        j=0
        k=len(needle)
        temp=''
        while j<len(haystack):
            temp+=haystack[j]
            
            if j-i+1<k:
                j+=1
                
            elif j-i+1==k:
                if temp==needle:
                    return i
                temp=temp[1:]
                i+=1
                j+=1
        return -1