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
    def remove_node(self, n, d, p = None):
        current_node = n
        previous_node = p

        if current_node.get_data() == d:
            if previous_node is None:
                if current_node.get_next():
                    current_node = current_node.get_next()
                    self.size -= 1
                    return True
                else:
                    current_node = None
                    self.size = 0
                    return True
            else:
                if current_node.get_next():
                    previous_node.set_next(current_node.get_next())
                    self.size -= 1
                    return True
                else:
                    previous_node.set_next(None)
                    self.size -= 1
                    return True
        else:
            if current_node.get_next():
                previous_node = current_node
                current_node = current_node.get_next()
                return self.remove_node(current_node, d, previous_node)
            else:
                return False

    # reverse link list
    def reverse_list(self, c, p = None):
        current_node = c
        previous_node = p

        if current_node.get_next() is None:
            if previous_node is not None:
                self.set_head(current_node)
                current_node.set_next(previous_node)
            else:
                self.set_head(current_node)
                current_node.set_next(None)
        else:
            if previous_node is not None:
                temp_current, temp_previous = current_node.get_next(), current_node
                current_node.set_next(previous_node)
                self.reverse_list(temp_current, temp_previous)
            else:
                temp_current, temp_previous = current_node.get_next(), current_node
                current_node.set_next(None)
                self.remove_node(temp_current, temp_previous)

    # TODO: insert at nth position or nth position from the end


# test sll
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

    def test_remove_node(self):
        mySll = Singly_Linked_List()
        mySll.prepend_node(1)
        mySll.prepend_node(3)
        mySll.prepend_node(10)
        mySll.prepend_node(5)
        result = mySll.remove_node(mySll.get_head(), 10)
        self.assertIsNone(mySll.find_node(mySll.get_head(), 10))
        self.assertTrue(result)

    def test_reverse_list(self):
        mySll = Singly_Linked_List()
        mySll.prepend_node(1)
        mySll.prepend_node(3)
        mySll.prepend_node(10)
        mySll.prepend_node(5)
        mySll.reverse_list(mySll.get_head())
        result = mySll.find_node(mySll.get_head(), 5)
        self.assertIsNone(result.get_next())
        # self.assertEqual(mySll.get_head().get_data(), 1)

# run test
if __name__ == '__main__':
    test.main()
