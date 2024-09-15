import time
s=time.time()
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.str=None
    def addb(self,data):
        ptr=node(data)
        ptr.next=self.str
        if self.str==None:
            ptr.next=self.str
        self.str=ptr
    def deleteb(self):
        if self.str==None:
            print("empty")
        else:
            self.str=self.str.next
    def addend(self,data):
        ptr=node(data)
        if self.str==None:
            ptr.next=self.str
        else:
             temp=self.str
             while(temp.next!=None):
                 temp=temp.next
             temp.next=ptr
    def deleteend(self):
        if self.str==None:
            print("it is empty")
        else:
            temp=self.str
            while temp.next!=None:
                prev=temp
                temp=temp.next
            prev.next=None
    def display(self):
        if self.str==None:
            print("its empty")
        else:
            temp=self.str
            while temp!=None:
                print(temp.data)
                temp=temp.next
l=linkedlist()
print("""1.addb
2.deleteb
3.addend
4.deleteend
5.display""")

while True:
    n=int(input("enter the choice"))
    if n==1:
        element=int(input("enter the data"))
        l.addb(element)
    elif n==2:
        l.deleteb()
    elif n==3:
        l.addend(12)
    elif n==4:
        l.deleteend()
    elif n==5:
        l.display()
    elif n==6:
        break
    else:
        print("valid number")
e=time.time()
print("the time taken:",e-s)
        
        
        

    
