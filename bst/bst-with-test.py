import unittest as test

class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
    
    def get_data(self):
        return self.data

    def get_left(self):
        return self.left
    def set_left(self, d):
        self.left = Node(d)

    def get_right(self):
        return self.right
    def set_right(self, d):
        self.right = Node(d)

class BST(object):
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    def set_root(self, r):
        self.root = r
    
    # insert
    def insert_node(self, c, d):
        current_node = c

        if self.root is None:
            self.set_root(Node(d))
        else:
            if current_node.get_data() > d:
                if current_node.get_left():
                    self.insert_node(current_node.get_left(), d)
                else:
                    current_node.set_left(d)
            else:
                if current_node.get_right():
                    self.insert_node(current_node.get_right(), d)
                else:
                    current_node.set_right(d)
    
    # find node
    def find_data(self, c, d):
        current_node = c
        result = None

        if current_node.get_data() == d:
            result = current_node.get_data()
        else:
            if current_node.get_data() > d:
                if current_node.get_left() is not None:
                    result = self.find_data(current_node.get_left(), d)
            else:
                if current_node.get_right() is not None:
                    result = self.find_data(current_node.get_right(), d)
        
        return result



# tests
class test_bst(test.TestCase):
    
    def test_bst(self):
        result = BST()

        # test empty bst
        self.assertIsNone(result.get_root())

        # test insert first node
        result.insert_node(result.get_root(), 15)
        self.assertIsNotNone(result.get_root())
        self.assertEqual(result.get_root().get_data(), 15)
        self.assertIsNone(result.get_root().get_left())
        self.assertIsNone(result.get_root().get_right())

        # test insert more nodes
        result.insert_node(result.get_root(), 5)
        result.insert_node(result.get_root(), 10)
        result.insert_node(result.get_root(), 25)
        result.insert_node(result.get_root(), 20)
        result.insert_node(result.get_root(), 30)
        self.assertIsNotNone(result.get_root())
        self.assertEqual(result.get_root().get_data(), 15)
        self.assertIsNotNone(result.get_root().get_left())
        self.assertIsNotNone(result.get_root().get_right())
        self.assertEqual(result.get_root().get_left().get_data(), 5)
        self.assertEqual(result.get_root().get_right().get_data(), 25)

        # find node:
        self.assertIsNone(result.find_data(result.get_root(), 2))
        self.assertEqual(result.find_data(result.get_root(), 30), 30)

# run default
if __name__ == '__main__':
    test.main()