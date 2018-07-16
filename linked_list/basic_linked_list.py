'''
https://www.youtube.com/watch?v=JlMyYuY1aXU&index=2&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7
'''

class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            current_node = current_node.next
            total += 1
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index>self.length():
            print('ERROR')
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self,index):
        if index>self.length():
            print('ERROR')
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

ll = LinkedList()
print(ll.display())
ll.append(1)
ll.append(2)
print(ll.display())