class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out=[0]*len(s)
        for i in range(len(s)):
            out[indices[i]]=s[i]
        return ''.join(out)