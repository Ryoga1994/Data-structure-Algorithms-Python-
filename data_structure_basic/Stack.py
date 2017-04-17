class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        """insert value on to top of stack"""
        new_node = Node(value,self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        """remove the top value and return it"""
        curr = self.top
        self.top = self.top.next
        self.size -= 1
        return(curr.value)


    def peek(self):
        """return the top value"""
        return(self.top.value)

def main():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.size
    stack.pop()
