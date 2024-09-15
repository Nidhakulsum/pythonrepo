import time
s=time.time()
def bubble(list):
    n=len(list)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[20,10,90,5]
print(bubble(list))
e=time.time()
print("time taken",e-s)
            
    
