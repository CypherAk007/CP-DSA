from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        arr=[]
        for i in range(N):
            arr.append([S[i],F[i],i+1])
        # print(arr)
        arr.sort(key=lambda x:x[1])
        # print(arr)
        ansst=0
        ansend=0
        out=[]
        for i in range(0,N):
            s=arr[i][0]
            e=arr[i][1]
            idx=arr[i][2]
            if s>ansend:
                ansend=e
                out.append(idx)
        out.sort()
        return out
                
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends