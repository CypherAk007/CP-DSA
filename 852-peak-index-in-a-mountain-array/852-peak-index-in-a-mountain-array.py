class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        # Brute Force
        for i in range(1,len(a)-1):
            if a[i]>a[i-1] and a[i]>a[i+1]:
                return i
            