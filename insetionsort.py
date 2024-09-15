def insertion(l):
    for i in range(1,len(l)):
        j=i
        while l[j-1]>l[j] and j>0:
            l[j-1],l[j]=l[j],l[j-1]
            j=j-1
    return l
l=[20,5,9,3,1]
print(insertion(l))
