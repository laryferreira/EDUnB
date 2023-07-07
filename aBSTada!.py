class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def inorder(self):
        if self:
            if self.left:
                for el in self.left.inorder():
                    yield el
            yield self.key
            if self.right:
                for el in self.right.inorder():
                    yield el
    
    def postorder(self):
        if self:
            if self.left:
                for el in self.left.postorder():
                    yield el
            if self.right:
                for el in self.right.postorder():
                    yield el
            yield self.key
    
    def preorder(self):
        if self:
            yield self.key
            if self.left:
                for el in self.left.preorder():
                    yield el
            if self.right:
                for el in self.right.preorder():
                    yield el
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def traversal(self, type): 
        if self.root:
            if type == "inorder":
                return self.root.inorder()
            elif type == "postorder":
                return self.root.postorder()
            elif type == "preorder":
                return self.root.preorder()
        else:
            return []

    def add(self, key):
        if self.root:
            self.grow(key, self.root)
        else:
            self.root = TreeNode(key)
        self.size += 1

    def grow(self, key, node):
        if key < node.key:
            if node.left:
                self.grow(key, node.left)
            else:
                node.left = TreeNode(key, parent=node)
        elif key > node.key:
            if node.right:
                self.grow(key, node.right)
            else:
                node.right = TreeNode(key, parent=node)
        else:
            node.key = key
                
                
bst = BinarySearchTree()
command = input()

while (command != "quack"):
    out = ""
    if command.isnumeric():
        bst.add(int(command))
    else:
        if bst.size > 0:
            if command == "in":
                out = " ".join([str(key) for key in bst.traversal("inorder")])
            elif command == "pre":
                out = " ".join([str(key) for key in bst.traversal("preorder")])
            elif command == "pos":
                out = " ".join([str(key) for key in bst.traversal("postorder")])
        print(out)
    command = input()
