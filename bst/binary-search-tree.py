class Node:
    """
    Tree node: left and right child + data which can be of any object
    """
    def __init__(self, val):
        """
        Node constructor
        """
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, val):
        """
        Insert new node with data
        """
        if self.val:
            if val < self.val:
                if self.left_child is None:
                    self.left_child = Node(val)
                else:
                    self.left_child.insert(val)
            elif val > self.val:
                if self.right_child is None:
                    self.right_child = Node(val)
                else:
                    self.right_child.insert(val)
        else:
            self.val = val

    def find_node(self, val, parent=None):
        """
        find node containing data
        """
        if val < self.val:
            if self.left_child is None:
                return None, None
            return self.left_child.find_node(val, self)
        elif val > self.val:
            if self.right_child is None:
                return None, None
            return self.right_child.find_node(val, self)
        else:
            return self, parent

    def delete_node(self, val):
        """
        delete node containing data
        """
        # find node containing data
        node, parent = self.find_node(val)
        if node is not None:
            children_count = node.children_count()
        
        if children_count == 0:
            # if the node has no children, remove node
            if parent:
                if parent.left_child is node:
                    parent.left_child = None
                else:
                    parent.right_child = None
                del node
            else:
                self.val = None
        elif children_count == 1:
            # if node has 1 child, replace node with its child
            if node.left_child:
                temp_node = node.left_child
            else:
                temp_node = node.right_child
            if parent:
                if parent.left_child is temp_node:
                    parent.left_child = None
                else:
                    parent.right_child = None
                del node
            else:
                self.left_child = temp_node.left_child
                self.right_child = temp_node.right_child
                self.val = temp_node.val
    
    def children_count(self):
        """
        return the number of children
        """
        count = 0
        if self.left_child:
            count += 1
        if self.right_child:
            count += 1
        return count

sampleData = [8, 3, 10, 1, 6, 4, 7, 14, 13]

def setup(data):
    root = Node(8)
    for val in data:
        root.insert(val)
    return root

root = setup(sampleData)
node, parent = root.find_node(14)
root.delete_node(1)
print("Node:", node.val, "Parent:", parent.val, "total Nodes:")
