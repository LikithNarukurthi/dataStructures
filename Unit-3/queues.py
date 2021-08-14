class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        if self.rear is None:
            self.front = self.rear = Node(data, None)
            return

        self.rear.next = Node(data, None)
        self.rear.next.prev = self.rear
        self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            raise Exception('empty queue')
        temp = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
            return
        self.front.prev = None

        return temp

    def clearqueue(self):
        self.front = self.rear = None

    def emptyqueue(self):
        if self.front is None:
            return True
        return False

    def display(self):
        itr = self.front
        sstr = ' '
        while itr:
            sstr += str(itr.data) + '-->'
            itr = itr.next
        print(sstr)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    queue.display()
