import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # creating the adj list given roads roads[i] = [ui, vi, timei]
        adj=[[] for i in range(n)]
        for it in roads:
            # undirected graph
            adj[it[0]].append([it[1],it[2]])
            adj[it[1]].append([it[0],it[2]])
            
        modulo=1000000007
        
        heap=[] #[dist,node]
        dist=[float('inf')]*n
        ways=[0]*n # stores the no. of ways to reach a node
        # init
        dist[0]=0
        ways[0]=1
        heapq.heappush(heap,[0,0])
        
        while(len(heap)!=0):
            x=heapq.heappop(heap)
            dis=x[0]
            node=x[1]
            
            for it in adj[node]:
                adjNode=it[0]
                adjwt=it[1]
                
                # This was the first time i came with
                # this short distance
                if (dis+adjwt<dist[adjNode]):
                    dist[adjNode]=dis+adjwt
                    heapq.heappush(heap,[dis+adjwt,adjNode])
                    ways[adjNode]=ways[node]
                # if we have reached the already vis path 
                # with same path lenght then only add the ways 
                # to current ways
                elif (dis+adjwt==dist[adjNode]):
                    ways[adjNode]=(ways[adjNode]+ways[node])%modulo
                    
        # return the dest ways
        return (ways[n-1])% modulo
        