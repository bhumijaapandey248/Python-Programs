#https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

def rotateArray_clockWise( n, x,arr):
    a= arr[x:n:1]
##    print(a)
    b= arr[0:x:1]
    ##print(b)
    c= a+b
    return c

t= int(input())
while(t>0):
    s1 = input().split()
    n =s1[0]
    n =int(n)
    x =s1[1]
    x = int(x)
    s = input()
    lst = s.split()
    arr = list(map(int,lst)) 
    index = rotateArray_clockWise( n, x,arr)
    for i in index:
        print(i,end=' ')
    print()
    t=t-1
    
    
