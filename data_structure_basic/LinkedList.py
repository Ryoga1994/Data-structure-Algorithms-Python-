class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,value):
        """insert at the head of the list"""
        curr = Node(value,self.head)
        self.head = curr
        self.size += 1

    def print_list(self):
        """print all values in list"""
        curr = self.head
        while(curr):
            print(str(curr.value)+" ")
            curr = curr.next

    def delete(self):
        """delete first node in list and return the value"""
        if(self.size==0):
            print("Empty list, nothing to delete.")
        else:
            old_head = self.head
            self.head = self.head.next
            self.size -= 1
            return(old_head.value)



def main():
    list = LinkedList()
    list.insert(3)
    list.insert(5)
    list.delete()
    list.print_list()
