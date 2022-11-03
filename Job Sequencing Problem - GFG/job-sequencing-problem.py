#User function Template for python3
# class Job {
#     int id, profit, deadline;
#     Job(int x, int y, int z){
#         this.id = x;
#         this.deadline = y;
#         this.profit = z; 
#     }
# }
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        # covert into arr [profit,id,deadline]
        arr=[]
        for val in Jobs:
            temp=[]
            temp.append(val.profit)
            temp.append(val.id)
            temp.append(val.deadline)
            arr.append(temp)
        # print(arr)
        
        # sort based on the profit desc order
        arr.sort(key=lambda x:x[0],reverse=True)
        
        maxiDeadline=float('-inf')
        for i in range(n):
            maxiDeadline=max(maxiDeadline,arr[i][2])
        # print(maxiDeadline)
        
        schedule=[-1]*(maxiDeadline+1) #make schedule arr of 1-based indexing
        
        count=0
        maxProfit=0 
        for i in range(n):
            currProfit=arr[i][0]
            currJobId=arr[i][1]
            currDead=arr[i][2]
            
            for k in range(currDead,0,-1):
                if schedule[k]==-1:
                    count+=1
                    maxProfit+=currProfit
                    schedule[k]=currJobId
                    break
                
        ans=[]
        ans.append(count)
        ans.append(maxProfit)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
