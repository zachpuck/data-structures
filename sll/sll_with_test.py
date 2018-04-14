# input unittest module as test
import unittest as test

# node class
class Node(object):
    def __init__(self, d):
        self.data = d
        self.next_node = None

    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
    
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n

# link list class
class Singly_Linked_List(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get_head(self):
        return self.head
    def set_head(self, h):
        self.head = h

    def get_size(self):
        return self.size

    # add new node at beginning
    def prepend_node(self, d):
        if self.head is None:
            self.head = Node(d)
            self.size += 1
        else:
            new_node = Node(d)
            new_node.set_next(self.head)
            self.head = new_node
            self.size += 1

    # # find node
    def find_node(self, n, d):
        current_node = n

        if current_node.get_data() == d:
            return current_node
        else:
            if current_node.get_next():
                current_node = current_node.get_next()
                return self.find_node(current_node, d)


    # append new node to end of linked list
    def append_node(self, n, d):
        current_node = n

        if current_node.get_next() is None:
            new_node = Node(d)
            current_node.set_next(new_node)
            self.size += 1
        else:
            current_node = current_node.get_next()
            self.append_node(current_node, d)
            
    # remove node

# test ssl
class Test_ssl_with_test(test.TestCase):

    def test_new_ssl(self):
        result = Singly_Linked_List()
        self.assertIsNone(result.get_head())
        self.assertEqual(result.get_size(), 0)

    def test_prepend_node(self):
        result = Singly_Linked_List()
        result.prepend_node(1)
        self.assertIsNotNone(result.get_head())
        self.assertEqual(result.get_size(), 1)
        self.assertEqual(result.get_head().get_data(), 1)
        self.assertIsNone(result.get_head().get_next())

    def test_find_node(self):
        mySll = Singly_Linked_List()
        mySll.prepend_node(1)
        mySll.prepend_node(5)
        mySll.prepend_node(3)
        mySll.prepend_node(10)
        result = mySll.find_node(mySll.get_head(), 3)
        self.assertEqual(result.get_data(), 3)

    def test_append_node(self):
        mySll = Singly_Linked_List()
        mySll.prepend_node(1)
        mySll.prepend_node(3)
        mySll.append_node(mySll.get_head(), 6)
        result = mySll.find_node(mySll.get_head(), 6)
        self.assertEqual(mySll.get_head().get_data(), 3)
        self.assertEqual(result.get_data(), 6)
        self.assertIsNone(result.get_next())

    #TODO: test append_node with many more items in node

# run test
if __name__ == '__main__':
    test.main()

# mySLL = Singly_Linked_List()
# mySLL.prepend_node(15)
# mySLL.prepend_node(3)
# current_node = mySLL.get_head().get_next()
# print(current_node.get_data())