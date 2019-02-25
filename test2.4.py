##4.	Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
##Sample List: ['abc', 'xyz', 'aba', '1221']
##Expected Result: 2

lis=['abc', 'xyz', 'aba', '1221']
lis1=[]
for i in lis:
    if i[0]==i[-1]:
        lis1.append(i)
print(len(lis1))

