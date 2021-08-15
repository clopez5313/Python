# A node class for the Tree.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Method to add a new node to the Tree.
    def insert(self, data):
        # Check if the node is not null.
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrder(self, root):
        result = []
        if root:
            result = self.inOrder(root.left)
            result.append(root.data)
            result = result + self.inOrder(root.right)

        return result

    def preOrder(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.preOrder(root.left)
            result = result + self.preOrder(root.right)

        return result

    def postOrder(self, root):
        result = []
        if root:
            result = self.postOrder(root.left)
            result = result + self.postOrder(root.right)
            result.append(root.data)

        return result

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=" ")
        if self.right:
            self.right.printTree()

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("In-order Traversal:", root.inOrder(root))
print("Pre-order Traversal:", root.preOrder(root))
print("Post-order Traversal:", root.postOrder(root))
