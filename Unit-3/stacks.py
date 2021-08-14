# from collections import deque


# class Stack:
#     def __init__(self):
#         self.container = deque()

#     def peek(self):
#         return self.container[-1]

#     def push(self, value):
#         self.container.append(value)

#     def pop(self):
#         return self.container.pop()

#     def is_empty(self):
#         return len(self.container) == 0

#     def size(self):
#         return len(self.container)


# def reverse_string(str_input):
#     stack = Stack()
#     for i in str_input:
#         stack.push(i)
#     tms = ''
#     for i in range(stack.size()):
#         tms += stack.pop()
#     print(tms)


# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }

#     return match_dict[ch1] == ch2


# def is_balanced(str_input):
#     stack = Stack()
#     paracl = [']', ')', '}']
#     paraop = ['{', '(', '[']

#     for i in str_input:
#         if i in paraop:
#             stack.push(i)
#         if i in paracl:
#             if stack.size() == 0:
#                 return False
#             if not is_match(i, stack.pop()):
#                 return False

#     return (stack.size() == 0)


# if __name__ == "__main__":
#     reverse_string('We will conquere COVID-19')
#     print(is_balanced("))((a+b}{"))
#     print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            return
        self.top = Node(data, self.top)

    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.data

    def peek(self):
        return self.top.data

    def clearstack(self):
        self.top = None

    def emptystack(self):
        if self.top is None:
            return True
        return False

    def display(self):
        itr = self.top
        sstr = ' '
        while itr:
            sstr += str(itr.data) + '-->'
            itr = itr.next
        print(sstr[:-3])


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.pop())
    print(stack.peek())
    stack.display()
