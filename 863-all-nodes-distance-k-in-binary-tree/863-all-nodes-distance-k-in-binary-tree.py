# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 1->mark the parent
        parent_track={}#stores the parent ptrs
        self.markParent(root,parent_track,target)
        
        # 2->radially traverse upward  left right by a distance 1 everytime
        visited={}
        queue=[]
        queue.append(target)#init
        visited[target]=True
        cur_level=0#distance fm the node
        while len(queue)!=0:
            size=len(queue)
            if cur_level==k:
                break
            cur_level+=1
            for i in range(size):
                current=queue.pop(0)
                # we check for left right and up/parent
                if current.left!=None and current.left not in visited:
                    queue.append(current.left)
                    visited[current.left]=True
                if current.right!=None and current.right not in visited:
                    queue.append(current.right)
                    visited[current.right]=True 
                if parent_track.get(current)!=None and parent_track.get(current) not in visited:
                    queue.append(parent_track[current])
                    visited[parent_track[current]]=True
        # now the left out nodes in the queue is the k nodes 
        result=[]
        while(len(queue)!=0):
            current=queue.pop(0)
            result.append(current.val)
        return result
        
        
    def markParent(self,root,parent_track,target):
        # simple lvl order traversal
        queue=[]
        queue.append(root)
        while(len(queue)!=0):
            current=queue.pop(0)
            
            if current.left:
                parent_track[current.left]=current
                queue.append(current.left)
            if current.right:
                parent_track[current.right]=current
                queue.append(current.right)
        
        