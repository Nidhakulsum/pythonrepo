class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None
class doublelinkedlist:
    def __init__(self):
       self.str = None
       
    def insertatbegin(self, data):
        ptr = Node(data)
        if self.str==None:
            self.str = ptr
        else:
            ptr.next = self.str
            self.str.previous = ptr
            self.str = ptr
    def deleteatbegin(self):
        if self.str==None:
            print("its empty")
        else:
            temp=self.str
            self.str=temp.next
    def insertatend(self, data):
        ptr= Node(data)
        if self.str==None:
            self.insertAtBeginning(data)
        else:
            temp = self.str
            while temp.next is not None:
                temp = temp.next
            temp.next = ptr
            ptr.previous = temp
    def deleteatend(self):
        if self.str==None:
            print("noo noo")
        else:
            temp=self.str
            while temp.next!=None:
                temp=temp.next
            temp.previous.next=None
    def display(self):
        temp = self.str
        while temp is not None:
            print(temp.data)
            temp = temp.next
db=doublelinkedlist()
print("""1.addb
2.deleteb
3.addend
4.deleteend
5.display""")
while True:
    n=int(input("enter the choice"))
    if n==1:
        element=int(input("enter the data"))
        db.insertatbegin(element)
    elif n==2:
        db.deleteatbegin()
    elif n==3:
        element1=int(input("enter the data"))
        db.insertatend(element1)
    elif n==4:
        db.deleteatend()
    elif n==5:
        db.display()
    elif n==6:
        break
    else:
        print("valid number")
