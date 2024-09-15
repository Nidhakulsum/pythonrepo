def ls(list,key):
    n=len(list)
    found=0
    for i in range(0,n):
        if list[i]==key:
            found=1
            break
    if found==1:
        print("found")
    else:
        print("no")
        
list=[10,23,56,78,2]
print(list)
key=int(input("enter the key"))
print(ls(list,key))
            
