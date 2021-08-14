class Node:    
    def __init__(self,data):    
        self.data = data    
        self.next = None    
     
class CreateList:    
  #Declaring head and tail pointer as null.    
    def __init__(self):    
        self.head = Node(None)   
        self.tail = Node(None)    
        self.head.next = self.tail    
        self.tail.next = self.head    
        
  #This function will add the new node at the end of the list.    
    def add(self,data):    
        newNode = Node(data) 
    #Checks if the list is empty.    
        if self.head.data is None:      
            self.head = newNode   
            self.tail = newNode    
            newNode.next = self.head    
        else:    
      #tail will point to new node.    
            self.tail.next = newNode    
      #New node will become new tail.    
            self.tail = newNode    
      #Since, it is circular linked list tail will point to head.    
            self.tail.next = self.head    
     
  #Displays all the nodes in the list    
    def display(self):    
        current = self.head   
        if self.head is None:    
            print("List is empty")   
            return    
        else:    
            print("Nodes of the circular linked list: ")   
        #Prints each node by incrementing pointer.    
            print(current.data)   
        while(current.next != self.head):    
            current = current.next  
            print(current.data)         
cl = CreateList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    cl.add(data)
print('The linked list: ', end = '')   
cl.display()  