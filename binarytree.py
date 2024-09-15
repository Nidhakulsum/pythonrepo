class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
    if self.data is None:
        self.data=data
    else:
        if data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        elif data >self.data:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)
    

# Print the tree
 
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
  # Postorder traversal
# Left ->Right -> Root
   # Postorder traversal
# Left ->Right -> Root
   def PostorderTraversal(self, root):
      res = []
      if root:
         res = self.PostorderTraversal(root.left)
         res = res + self.PostorderTraversal(root.right)
         res.append(root.data)
      return res
            
                
while True:
    print("***WELCOME TO BINARY TREE TRAVERSE***")
    print("please select the options below")
    print("")
    print('''
    1.INSERTION OF NODES
    2.INORDER TRAVERSE
    3.PREORDER TRAVERSE
    4.POSTORDER TRAVERSE
    5.EXIT''')
    print("")
    op=int(input("the option you want to execute: "))
    if op==1:
         t=int(input("enter the root of your tree: "))
         root=Node(t)
         n=int(input("how many node you want to enter: "))
         for i in range(0,n):
             a=int(input(""))
             b=root.insert(a)
           
             print("your nodes are inserted successfully")
    elif op==2:
        try:
           print(root.inorderTraversal(root))
           print("succesfully inorder exist")
        except NameError:
            print("your binary tree is empty please enter the values")
            
        
    elif op==3:
        try:
           print("this is preorder of ur binary tree")
           print(root.PostorderTraversal(root))
        except NameError:
           print("your binary tree is empty please enter the values")
    elif op==4:
        print("this is post orderof ur binary tree")
        root.postorder()

    elif op==5:
        exit()
    else:
        print("please enter the correct option")
    

