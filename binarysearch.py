import time
s=time.time()
def  binary(list,key):
    n=len(list)
    low=0
    high=n-1
    found=0
    while(low<=high):
        mid=(low+high)//2
        if list[mid]==key:
            found=1
            break
        elif key >mid:
            low=mid+1
        else:
            high=mid-1
    if found==1:
        print("found")
    else:
        print("not")
list=[20,50,90,5]
print(list)
key=int(input("enetr key"))
print(binary(list,key))
e=time.time()
print("time taken:",e-s)
