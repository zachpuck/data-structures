import unittest as test

class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
    
    def get_data(self):
        return self.data

class BST(object):
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    def set_root(self, r):
        self.root = r
    
    # insert

# tests
class test_bst(test.TestCase):
    def test_new_bst(self):
        result = BST()
        self.assertEqual(result.get_root(), None)

# run default
if __name__ == '__main__':
    test.main()