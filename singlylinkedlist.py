import time
s=time.time()
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.str=None
    
    def addatlast(self,data):
         if (self.str==None):
             self.str=data  
         else:
             temp=self.str
             while(temp.next!=None):
                 temp=temp.next
             temp.next=data
    def deleteatlast(self):
         if (self.str==None):
             print("empty")
         else:
             temp=self.str
             while(temp.next!=None):
                 prev=temp
                 temp=temp.next
             prev.next=None
    
    def deleteatbegin(self):
        if (self.str==None):
            print("empty")
        else:
            temp=self.str
            self.str=temp.next
   
  
    def addbegin(self,data):
        if (self.str==None):
            self.str=data
        else:
            data.next=self.str
            self.str=data
            
    def display(self):
        if (self.str==None):
            print("empty")
        else:   
            temp=self.str
            while(temp!=None):
                print(temp.data)
                temp=temp.next
            
l=linkedlist()
l1=int(input("enter the list lengtg"))
print("one by one element")
for i in range(l1):
    data=int(input(" "))
    nk=node(data)
    l.addatlast(nk)
print("""1.to insert at last
2.to delete at begin
3. to insert at beiglast
4. to delete at last
5.display""")

while True:
    ch=int(input("enter the choice"))
    if ch==1:
        data=int(input("enter th data whivh u insert"))
        nk=node(data)
        l.addatlast(nk)
        e=time.time()
        print("time taken:",e-s)
    
    elif ch==2:
        l.deleteatbegin()
        e=time.time()
        print("time taken:",e-s)
    elif ch==3:
        data=int(input("enter th data whivh u insert"))
        nk=node(data)
        l.addbegin(nk) 
    elif ch==4:
        l.deleteatlast()
        e=time.time()
        print("time taken:",e-s)
    elif ch==5:
        l.display()
    elif ch==6:
        print("exit")
    else:
        print("valid choice")
        break
e=time.time()
print("time taken:",e-s)

    

            
        
                
