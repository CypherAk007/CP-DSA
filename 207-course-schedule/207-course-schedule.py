class Solution:
    def canFinish(self,V,prerequisites):
        #code here
        adj=[[] for i in range(V)]
        for it in prerequisites:
            adj[it[1]].append(it[0])
            
        # check for the toposort
        indegree=[0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
        
        # push all the ele with indegree=0 into the queue
        q=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        
        topo=[]
        while(q):
            node=q.pop(0)
            topo.append(node)
            # now node is in the topological sort so remove the
            # it from the indegree
            
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
                    
        if len(topo)==V:return topo
        return []
        