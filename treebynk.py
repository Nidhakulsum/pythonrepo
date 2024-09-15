class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
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

    def inorder(self, root):
        r = []
        if root:
            r = self.inorder(root.left)
            r.append(root.data)
            r = r + self.inorder(root.right)
        return r

    def preorder(self, root):
        r = []
        if root:
            r.append(root.data)
            r = r + self.preorder(root.left)
            r = r + self.preorder(root.right)
        return r

    def postorder(self, root):
        r = []
        if root:
            r = self.postorder(root.left)
            r = r + self.postorder(root.right)
            r.append(root.data)
        return r

print('''
    1. INSERTION OF NODES
    2. INORDER TRAVERSE
    3. PREORDER TRAVERSE
    4. POSTORDER TRAVERSE
    5. EXIT''')
print("")
def opt1():
        n = int(input("enter the root of your tree: "))
        root = Node(n)
        ls = []
        h = int(input("how many nodes you want to enter: "))
        for i in range(h):
            a = int(input(""))
            root.insert(a)
        print("Your nodes are inserted successfully")
    
def option():
    print("")
    print("============WELCOME TO THE WORLD OF BINARY TREE TRAVERSE============")
    print("")
    print("please select the options below")
    print("")
    op = int(input("the option you want to execute: "))
    if op==1:
        opt1()
    elif op == 2:
        try:
            print("The inorder traverse of the binary tree is", root.inorder(root))
        except NameError:
            print("your binary tree is empty please enter the values")
            opt1()
    elif op == 3:
        try:
            print("The preorder traverse of the binary tree is", root.preorder(root))
        except NameError:
            print("your binary tree is empty please enter the values")
            opt1()
    elif op == 4:
        try:
            print("The postorder traverse of the binary tree is", root.postorder(root))
        except NameError:
            print("your binary tree is empty please enter the values")
            opt1()
    elif op == 5:
        exit()
    else:
        print("Please enter the correct option")

option()
