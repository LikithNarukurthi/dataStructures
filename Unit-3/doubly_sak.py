class Node:
 def __init__(self, data):
   self.data = data
   self.next = None
   self.prev = None
class DoublyLinkedList:
 def __init__(self):
   self.head = None
 def push(self, new_data):
   new_node = Node(new_data)
   new_node.next = self.head
   if self.head is not None:
     self.head.prev = new_node
   self.head = new_node

 def insertAfter(self, prev_node, new_data):
   if prev_node is None:
     print ("the given previous node cannot be NULL")
     return
   new_node = Node(new_data)
   new_node.next = prev_node.next
   prev_node.next = new_node
   new_node.prev = prev_node
   if new_node.next is not None:
    new_node.next.prev = new_node

 def append(self,new_data):
   new_node = Node(new_data)
   new_node.next = None
   if self.head is None:
    new_node.prev = None
    self.head = new_node
    return

   last = self.head
   while(last.next is not None):
     last = last.next
   last.next = new_node
   new_node.prev = last
   return

 def printList(self, node):
  print( "\nTraversal in forward direction")
  while(node is not None):
    print (" % d" %(node.data), )
    last = node
    node = node.next
  print ("\nTraversal in reverse direction")
  while(last is not None):
    print (" %d " %(last.data), )
    last = last.prev
 def countNodes(self):  
        counter = 0
        current = self.head 
        while(current != None):  
            counter = counter + 1
            current = current.next
        return counter
 def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return True 
            current = current.next
        return False 


llist = DoublyLinkedList()
llist.append(1)
llist.push(2)
llist.push(3)
llist.append(4)
llist.insertAfter(llist.head.next, 5)
print( "Created DLL is: ", )
llist.printList(llist.head)
print("\nCount of nodes present in the list: " + str(llist.countNodes())) 
if llist.search(4): 
  print("Yes") 
else: 
  print("No")