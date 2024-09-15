def ls(list,key):
    n=len(list)
    for i in range(0,n):
        if list[i]==key:
            print("elemrnt found at index of",i)
            break
    else:
        print("not found")
list=[10,23,56,78,2]
print(list)
key=int(input("enter the key"))
print(ls(list,key))
            
