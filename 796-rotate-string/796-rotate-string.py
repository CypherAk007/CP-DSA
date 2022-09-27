class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp=s[:]
        while(True):
            s=s[1:]+s[0]
            if s==temp:
                return False
            if s==goal:
                return True
            