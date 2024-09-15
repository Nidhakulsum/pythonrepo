def hash(name):
    h=0
    for i in range(len(name)):
        f=ord(name[i])
        h=h+f*i
    return h%26
l=[]
name="nida"
l.append(name)
sem=3
l.append(sem)
print(hash(name))
