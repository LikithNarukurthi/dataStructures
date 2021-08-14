class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # the value part of the node
        self.next = next  # the pointer part of the node


class LinkedList:
    def __init__(self):
        self.head = None  # creating an empty linked list

    def Insert_at_beginning(self, data):
        # creating a node with a data part and the pointer to the next value i.e . the now head
        node = Node(data, self.head)
        self.head = node  # now the head points towards the new inserted element pushing the previous element behind

    def Insert_at_ending(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head # itr points to node(data,next) pointed by header
        while itr.next:
            itr = itr.next #itr points to next node(data,next)
        itr.next = Node(data) 

    def insert_values(self, value_list): # for inserting list of values
        self.head = None 
        for value in value_list:
            self.Insert_at_ending(value)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.Insert_at_ending(data)
            return
        itr = self.head
        count = 0 
        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):

        if index < 0 or index >= self.get_length():
            raise Exception('invalid index')

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert): 
        if self.head is None:
            return                                                      
        if self.head.data == data_after:  #self.head is header pointing to first node(data,next)
            self.head.next = Node(data_to_insert, self.head.next)
            return 
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
        if itr.next is None:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def display(self):
        if self.head is None:
            print('list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr[:-3])

    def search(self, data):
        itr = self.head 
        while itr.next: 
            if itr.data == data: 
                return True 
            itr = itr.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.display()
    ll.insert_after_value("orange", "apple")  # insert apple after mango
    ll.insert_after_value("banana", "apple")
    ll.display()
    ll.remove_by_value("banana")  # remove orange from linked list
    ll.display()
    '''ll.remove_by_value("figs")
    ll.display()
    ll.remove_by_value("banana")
    ll.display()
    print(ll.search("mango"))
    print("Count: ",ll.get_length())
    ll.remove_at(1)
    ll.display()
    #ll.insert_at(1,"guava")
    ll.display()
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print("Count: ",ll.get_length())
'''
    
