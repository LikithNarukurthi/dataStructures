class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.head=None

    def insert_on_top(self,data):
        node=Node(data,self.head)
        self.head=node
        print("Inserted Value: ",self.head.data)
        
    def insert_value(self,value_lst):
        for value in value_lst:
            self.insert_on_top(value)
        
        
    def remove_from_top(self):
        if self.head is None:
            print('Empty Stack')
            return
        else:
            print("Removed Value: ",self.head.data)
            self.head=self.head.next
            
        
if __name__=='__main__':
    stk=Stack()
    stk.insert_value([1,2,3])
    stk.remove_from_top()
    stk.remove_from_top()
    stk.remove_from_top()
    stk.remove_from_top()