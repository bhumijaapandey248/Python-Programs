l=[]
n=int(input("enter number of elments"))
##def enter(n):
for i in range(1,n+1):
    a=int(input())
    l.append(a)
print(l)
firstmax=l[0]
secondmax=l[0]
for i in range(1,n+1):
    if l[i]>firstmax:
        secondmax=firstmax
        firstmax=l[i]
    elif l[i]>secondmax:
        secondmax=l[i]
    else:
        pass
print(firstmax)
print(secondmax)

##r=int(input("enter number :"))
