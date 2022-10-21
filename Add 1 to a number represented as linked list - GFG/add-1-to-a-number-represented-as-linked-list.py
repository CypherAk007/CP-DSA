#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        head=self.reverseLL(head)
        
        carry=1
        temp=head
        while(temp!=None):
            val=temp.data+carry
            temp.data=val%10
            carry =val//10
            temp=temp.next
        head=self.reverseLL(head)
        while carry!=0:
            x=Node(carry%10)
            x.next=head
            head=x
            carry=carry//10
        
        return head
        
    def reverseLL(self,head):
        prev=None
        cur=head
        nxt=head
        while(cur!=None):
            nxt=nxt.next
            cur.next=prev
            prev=cur
            cur=nxt 
        head=prev
        return head
        
    def printf(self,head):
        temp=head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends