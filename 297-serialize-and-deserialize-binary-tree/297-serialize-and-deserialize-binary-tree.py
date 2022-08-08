# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return ''
        q=[]
        res=''
        q.append(root)
        while(len(q)!=0):
            # Always add left and right even if its null as we are considering its
            node=q.pop(0)
            if node==None:
                res+=('null ')
                continue
            res+=(str(node.val)+" ")
            q.append(node.left)
            q.append(node.right)
        return ''.join(map(str, res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='':return None
        q=[]
        values=data.split()
        print(values)
        root=TreeNode(values[0])
        q.append(root)
        i=1 
        while(i<len(values)):
            parent=q.pop(0)
            if values[i]!='null':
                left=TreeNode(int(values[i]))
                parent.left=left 
                q.append(left)
            i+=1 
            if values[i]!='null':
                right=TreeNode(int(values[i]))
                parent.right=right 
                q.append(right)
            i+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))