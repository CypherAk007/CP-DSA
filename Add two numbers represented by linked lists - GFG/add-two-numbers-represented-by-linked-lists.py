#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        t=0
        f=self.findLen(first)
        s=self.findLen(second)
        carry=0
        
        if f<s:
            carry=self.findSum(first)
            second=self.reverseLL(second)
            t=1
        else:
            carry=self.findSum(second)
            first=self.reverseLL(first)
            t=0
        
        if t:
            # self.printf(second)
            # print(carry)
            return self.addNum(second,carry)
            
        else:
            # self.printf(first)
            # print(carry)
            return self.addNum(first,carry)
            
    def addNum(self,head,carry):
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
        
    def findLen(self,head):
        l=0
        temp=head
        while(temp!=None):
            l+=1
            temp=temp.next
        return l

    def findSum(self,head):
        s=0
        temp=head
        while(temp!=None):
            s*=10
            s+=temp.data
            temp=temp.next
        return s
    
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
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends