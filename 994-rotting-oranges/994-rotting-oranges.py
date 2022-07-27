class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid==None or len(grid)==0:return 0
        rows=len(grid)
        cols=len(grid[0])
        queue=[]
        orgCount=0#cnt of all oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:#store init rotten oranges in the queue
                    queue.append([i,j])
                if grid[i][j]!=0:
                    orgCount+=1
                    
        if orgCount==0:return 0
        countMin=0#no. of days
        cnt=0 #stores the no. of org in queue
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        # bfs init starting
        while(len(queue)!=0):
            size=len(queue)
            cnt+=size
            for i in range(size):
                point=queue.pop(0)
                for j in range(4):
                    x=point[0]+dx[j]
                    y=point[1]+dy[j]
                    
                    if (x<0 or y<0 or x>=rows or y>=cols or grid[x][y]==0 or grid[x][y]==2): continue
                    
                    grid[x][y]=2
                    queue.append([x,y])
            if len(queue)!=0:
                countMin+=1
        if orgCount==cnt:
            return countMin
        else:
            return -1