class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        cur_node = self.root
        while True:
            if new_val < cur_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(new_val)
                    break 
            elif new_val > cur_node.value:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(new_val)
                    break
            else:
                break

    def search(self, find_val):
        cur_node = self.root
        while True:
            if find_val < cur_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    return False
            elif find_val > cur_node.value:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    return False
            else:
                return True
                
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)