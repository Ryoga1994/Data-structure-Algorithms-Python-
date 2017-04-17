class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size==0


    def enqueue(self,value):
        """add item to the end of the list"""
        newNode = Node(value,None)

        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

        self.size += 1

    def dequeue(self):
        if self.size==0:
            print("Empty queue!")
        else:

            del_node = self.head
            self.head = self.head.next
            self.size -= 1


    def print_queue(self):
        """print all values in list"""
        curr = self.head
        while(curr):
            print(str(curr.value)+" ")
            curr = curr.next



def main():
    q = Queue()
    q.enqueue(3)
    q.enqueue(6)
    q.dequeue()
    q.print_queue()