class node:
    def __init__(self,data):
        self.item=data
        self.next=None
        self.prev=None
        
class linkedlist:
    def __init__(self):
        self.str=None
     
    def addbegin(self,data):
        if (self.str==None):
            ptr=node(data)
            self.str=ptr
        else:
            print("empty")
    def addend(self,data):
        if self.str is None:
            ptr=node(data)
            self.str=ptr
            return
        n=self.str
        while n.next is not None:
            n=n.next
        ptr=node(data)
        n.next=ptr
        ptr.prev=n
            
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
            return
        self.str=self.str.next
        self.str_prev=None
           
   
  
    def display(self):
        if (self.str==None):
            print("empty")
            return
        else:   
            n=self.str
            while(n!=None):
                print(n.data)
                n=n.next
        print("\n")
            
l=linkedlist()
print("""1.to insert at start
2.to addend
3. to deletelast
4. to delete at begin
5.display""")

while True:
    ch=int(input("enter the choice"))
    if ch==1:
        l.addbegin(10)
        l.addbegin(110)
        l.addbegin(120)
        l.addbegin(100)
        
    elif ch==2:
        l.addend(40)
    elif ch==3:
      
        l.deleteatlast()
        
    elif ch==4:
        l.deleteatbegin()
    elif ch==5:
        l.display()
    elif ch==6:
        break
    else:
        print("valid choice")
    
    

            
        
                
