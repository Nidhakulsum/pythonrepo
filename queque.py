que=[]
def push():
    n=int(input("enter the elent"))
    que.append(n)
def remove():
    if len(que)==0:
        print("empty")
    else:
        que.pop(0)
def display():
    for i in range(0,len(que)):
        print(que[i])
print("""1.inser
2.pop
3.display
4.exit""")
while True:
    n1=int(input("enter the op"))
    if n1==1:
        print(push())
    elif n1==2:
        print(remove())
    elif n1==3:
        print(display())
    elif n1==4:
        break
    else:
        print("valid")


        
