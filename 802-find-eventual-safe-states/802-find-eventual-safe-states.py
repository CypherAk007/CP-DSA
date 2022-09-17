class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        vis=[0]*V
        patVis=[0]*V
        check=[0]*V #tells us all the safe nodes
        safeNodes=[]
        
        for i in range(V):
            if vis[i]==0:
                self.dfs(i,graph,vis,patVis,check)
        
        for i in range(V):
            if check[i]==1:
                safeNodes.append(i)
        return safeNodes
                
    def dfs(self,node,adj,vis,patVis,check):
        vis[node]=1
        patVis[node]=1
        check[node]=0
        for i in adj[node]:
            if vis[i]==0:
                if self.dfs(i,adj,vis,patVis,check)==True:
                    return True
            elif (patVis[i]):
                return True
        # When we dont reach a cycle then 
        check[node]=1
        patVis[node]=0
        return False
    
    
                