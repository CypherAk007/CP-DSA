import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int: 
        heap=[]
        n=len(heights)
        m=len(heights[0])
        
        dist=[[float('inf')]*m for i in range(n)]
        dist[0][0]=0
        heapq.heappush(heap,[0,0,0]) #[dist,r,c]
        
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        while(len(heap)!=0):
            it=heapq.heappop(heap)
            diff=it[0]
            row=it[1]
            col=it[2]
            
            # if we reached the dist
            if row==n-1 and col==m-1:
                return diff
            
            for i in range(0,4):
                nr=row+dr[i]
                nc=col+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m:
                    # 1st we take the max b/w the diff and newdiff
                    newEffort=max(abs(heights[row][col]-heights[nr][nc]),diff)   
                    # next we take the min of newEffort and curr existing in dist
                    if newEffort<dist[nr][nc]:
                        dist[nr][nc]=newEffort
                        heapq.heappush(heap,[newEffort,nr,nc])
        
        return 0 #unreachable