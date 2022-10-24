class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            x=i*i
            if x==num:
                return True
            if x>num:
                return False
        