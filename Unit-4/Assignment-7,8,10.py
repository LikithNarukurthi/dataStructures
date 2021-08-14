class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
class CircularList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head

    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head

    def remove(self,data):
        if self.head.data is None:
            print("List is Empty!")
        if self.head.data==data:
            self.head=self.head.next
        itr=self.head
        while itr.next:
            if itr.next.data == data:
                itr.next=itr.next.next
                break
            itr=itr.next

    def display(self):
        itr=self.head
        if self.head is None:
            print("List is Empty!")
        else:
            print("Nodes of the Circular List:")
            print(itr.data,end=" ")
            while (itr.next!=self.head):
                itr=itr.next
                print(itr.data,end=" ")
        print()


cl=CircularList()
cl.add(0)
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(6)
cl.add(7)
cl.add(4)
cl.add(5)
print("The linked list: ",end=" ")
cl.display()
cl.remove(6)
cl.remove(7)
cl.remove(0)
print("The linked list: ",end=" ")
cl.display()