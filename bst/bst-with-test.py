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

    # find max
    def find_max(self, c, result = 0):
        current_node = c

        if current_node.get_data():
            if current_node.get_data() > result:
                result = current_node.get_data()
                if current_node.get_right():
                    result = self.find_max(current_node.get_right(), result)
        
        return result

    # find min
    def find_min(self, c, result = None):
        current_node = c

        if result is None:
            result = current_node.get_data() + 1

        if current_node.get_data():
            if current_node.get_data() < result:
                result = current_node.get_data()
                if current_node.get_left():
                    result = self.find_min(current_node.get_left(), result)

        return result

    # find height of bst
    # breath vs depth first
    # level order traversal
    # preorder, inorder, postorder
    # check if binary tree is bst or not
    # delete node from bst
    # inorder successor in a bst

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
        result.insert_node(result.get_root(), 10)
        result.insert_node(result.get_root(), 20)
        result.insert_node(result.get_root(), 8)
        result.insert_node(result.get_root(), 12)
        result.insert_node(result.get_root(), 17)
        result.insert_node(result.get_root(), 25)
        self.assertIsNotNone(result.get_root())
        self.assertEqual(result.get_root().get_data(), 15)
        self.assertIsNotNone(result.get_root().get_left())
        self.assertIsNotNone(result.get_root().get_right())
        self.assertEqual(result.get_root().get_left().get_data(), 10)
        self.assertEqual(result.get_root().get_right().get_data(), 20)

        # find data:
        self.assertIsNone(result.find_data(result.get_root(), 2))
        self.assertEqual(result.find_data(result.get_root(), 25), 25)

        # find min:
        self.assertEqual(result.find_min(result.get_root()), 8)

        # find max:
        self.assertEqual(result.find_max(result.get_root()), 25)

# run default
if __name__ == '__main__':
    test.main()