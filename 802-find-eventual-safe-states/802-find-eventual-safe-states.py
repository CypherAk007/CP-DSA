class Solution:
    # USING BFS KHANS ALGO
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        adjRev=[[] for i in range(V)]
        indegree=[0]*V
        for i in range(0,V):
            # i-->it
            # convert to it-->i
            for it in graph[i]:
                adjRev[it].append(i)
                #this stores the indegree of i and not it as edges reversed
                indegree[i]+=1 
                
        # APPEND THE NODES WITH INDEGREE 0 INTO THE QUEUE
        q=[]
        safeNodes=[]
        for i in range(0,V):
            if indegree[i]==0:
                q.append(i)
        
        while(q):
            node=q.pop(0)
            safeNodes.append(node)
            for it in adjRev[node]:
                indegree[it]-=1
                if indegree[it]==0:
                    q.append(it)

        
        safeNodes.sort()
        return safeNodes
        
    # USING DFS 
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         V=len(graph)
#         vis=[0]*V
#         patVis=[0]*V
#         check=[0]*V #tells us all the safe nodes
#         safeNodes=[]
        
#         for i in range(V):
#             if vis[i]==0:
#                 self.dfs(i,graph,vis,patVis,check)
        
#         for i in range(V):
#             if check[i]==1:
#                 safeNodes.append(i)
#         return safeNodes
                
#     def dfs(self,node,adj,vis,patVis,check):
#         vis[node]=1
#         patVis[node]=1
#         check[node]=0
#         for i in adj[node]:
#             if vis[i]==0:
#                 if self.dfs(i,adj,vis,patVis,check)==True:
#                     return True
#             elif (patVis[i]):
#                 return True
#         # When we dont reach a cycle then 
#         check[node]=1
#         patVis[node]=0
#         return False
    
    
                