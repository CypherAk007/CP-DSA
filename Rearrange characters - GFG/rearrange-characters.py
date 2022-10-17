#User function Template for python3
import heapq
class Solution :
    def rearrangeString(self, s):
        # 1->we use dict to get count of the each char in str
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1 
            else:
                d[s[i]]=1 
        
        # 2->we need a maxheap to store the top to char acc to count on top
        heap=[]
        for k,v in d.items():
            heapq.heappush(heap,[-1*(v),k])
        
        result=''
        while(len(heap)>1):
            current=heapq.heappop(heap)
            nxt=heapq.heappop(heap)
            result+=current[1]
            result+=nxt[1]
            current[0]=abs(current[0])-1
            nxt[0]=abs(nxt[0])-1
            if current[0]>0:
                heapq.heappush(heap,[-1*current[0],current[1]])
            if nxt[0]>0:
                heapq.heappush(heap,[-1*nxt[0],nxt[1]])
            
        if len(heap)!=0:
            last=heapq.heappop(heap)
            if abs(last[0])>1:
                return ""
            result+=last[1]
        return ''.join(result)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
        
# } Driver Code Ends