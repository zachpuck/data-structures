# Singly Linked List
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add_data(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find_data(self, d):
        current_node = self.root
        while current_node:
            if current_node.get_data() == d:
                return d
            else:
                current_node = current_node.get_next()
        
    def remove_data(self, d):
        current_node = self.root
        previous_node = None
        while current_node:
            if current_node.get_data() == d:
                if previous_node:
                    previous_node.set_next(current_node.get_next())
                else:
                    self.root = current_node.get_next()
                self.size -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        return False


myList = LinkedList()
myList.add_data(5)
myList.add_data(6)
myList.add_data(13)
myList.add_data(10)
print(myList.get_size())
print(myList.remove_data(7))
print(myList.remove_data(13))
print(myList.get_size())