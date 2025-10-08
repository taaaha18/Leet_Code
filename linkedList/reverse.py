class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self, value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    def reverse(self):
        cur=self.head
        prev=None
        while cur:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode
        self.head=prev           

    def display(self):
        cur=self.head
        while cur:
            print(cur.value, end=" -> ")
            cur=cur.next 

L=LinkedList()
L.insert(1)
L.insert(2)
L.insert(3)
L.insert(4)
L.insert(5)

L.display()

L.reverse()
print("\nReversed Linked List:")
L.display()