##2.	Write a Python program to split a list every Nth element.
##Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
##Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
ap=[]

l1=l[0:13:3]
l2=l[1:13:3]
l3=l[2:13:3]
##print(l1)
##print(l2)
##print(l3)
ap.append(l1)
ap.append(l2)
ap.append(l3)
print(ap)
