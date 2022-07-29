class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we take the first string and compare it with others 
        res=''
        for i in range(len(strs[0])):
            for row in strs:
                if i==len(row) or row[i]!=strs[0][i]:#any string in strs can go out of bounds
                    return res        
            res+=strs[0][i]
        return res