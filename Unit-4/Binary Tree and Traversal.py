class Node:                                                   # Constructor.... to create a New Node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):                                  # Inserting a Node in Binary Tree
        if self.data:                                        # Compare the new value with the parent node
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
                                                            # -------Traversal technics-----                                                        
    def inorderTraversal(self, root):                       # Inorder traversal- Left -> Root -> Right
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):                      # Preorder traversal- Root -> Left -> Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):                     # Postorder traversal- Left ->Right -> Root
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def PrintTree(self):                                    # Print the tree
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def findval(self, keyval):                              # findval method to compare the value with nodes
        if keyval < self.data:
            if self.left is None:
                return str(keyval)+" Not Found"
            return self.left.findval(keyval)
        elif keyval > self.data:
            if self.right is None:
                return str(keyval)+" Not Found"
            return self.right.findval(keyval)
        else:
            return(str(self.data) + ' is found')


root = Node(50)                                            # Creating an instance of class Node
root.insert(30)                                            # Use the insert method to add nodes
root.insert(20)
root.insert(70)
root.insert(60)
root.insert(80)
root.insert(42)
root.PrintTree()
print("After Inorder Traversal------")
print(root.inorderTraversal(root))
print("After Preorder Traversal------")
print(root.PreorderTraversal(root))
print("After Postorder Traversal------")
print(root.PostorderTraversal(root))
print("Finding a value from a Tree!!!")
print(root.findval(7))
print(root.findval(14))