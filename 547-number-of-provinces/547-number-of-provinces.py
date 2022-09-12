class Solution:
    def findCircleNum(self, adj) -> int:
        # code here 
        V=len(adj)
        adjLs=[[] for i in range(V)]
        # print(adjLs)
        for i in range(0,V):
            for j in range(0,V):
                if adj[i][j]==1 and i!=j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        # print(adjLs)
        # print(adj)
        vis=[0]*V
        c=0
        for i in range(V):
            if vis[i]==0:
                c+=1
                self.dfs(i,adjLs,vis)
        return c
        
    def dfs(self,node,adjLs,vis):
        vis[node]=1
        for i in adjLs[node]:
            if vis[i]==0:
                self.dfs(i,adjLs,vis)