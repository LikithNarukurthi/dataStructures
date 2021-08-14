class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
  
# Class to create a Doubly Linked List 
class DoublyLinkedList: 
  
    # Constructor for empty Doubly Linked List 
    def __init__(self): 
        self.head = None
  
    # Given a reference to the head of a list and an 
    # integer, inserts a new node on the front of list 
    def insertatbegin(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put the data in it 
        new_node = Node(new_data) 
  
        # 3. Make next of new node as head and 
        # previous as None (already None) 
        new_node.next = self.head 
  
        # 4. change prev of head node to new_node 
        if self.head is not None: 
            self.head.prev = new_node 
  
        # 5. move the head to point to the new node 
        self.head = new_node 
  
    # Given a node as prev_node, insert a new node after 
    # the given node 
    def insertAfter(self, prev_node, new_data): 
  
        # 1. Check if the given prev_node is None 
        if prev_node is None: 
            print ("the given previous node cannot be NULL")
            return 
  
        # 2. allocate new node 
        # 3. put in the data 
        new_node = Node(new_data) 
  
        # 4. Make net of new node as next of prev node 
        new_node.next = prev_node.next
  
        # 5. Make prev_node as previous of new_node 
        prev_node.next = new_node 
  
        # 6. Make prev_node ass previous of new_node 
        new_node.prev = prev_node 
  
        # 7. Change previous of new_nodes's next node 
        if new_node.next is not None: 
            new_node.next.prev = new_node 
  
    # Given a reference to the head of DLL and integer, 
    # appends a new node at the end 
    def append(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put in the data 
        new_node = Node(new_data) 
  
        # 3. This new node is going to be the last node, 
        # so make next of it as None 
        new_node.next = None
  
        # 4. If the Linked List is empty, then make the 
        # new node as head 
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
  
        # 5. Else traverse till the last node 
        last = self.head 
        while(last.next is not None): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next = new_node 
  
        # 7. Make last node as previous of new node 
        new_node.prev = last 
  
        return
  
    # This function prints contents of linked list 
    # starting from the given node 
    def printList(self, node): 
  
    
        while(node is not None): 
            print (node.data,end= '<->')
            last = node 
            node = node.next
  
# Driver program to test above functions 
  
# Start with empty list 
llist = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    llist.append(data)
print ("Created DLL is: ", end=' ') 
llist.printList(llist.head) 
print("Enter the element to insert at begin:")
b=int(input())
llist.insertatbegin(b)  
print("After insert at begin:")
llist.printList(llist.head) 
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
print("enter the element to insert at a position:")
p=int(input())
print("After insert at pos:")
llist.insertAfter(llist.head.next, p) 
llist.printList(llist.head) 
  
