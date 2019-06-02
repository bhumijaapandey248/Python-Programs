#https://practice.geeksforgeeks.org/problems/pair-array-product-sum/0

def pair_array_product( n, arr ):
    count=0
    for i in range(0,n):

        for j in range(i+1,n):

            if(arr[i]+arr[j]<arr[i]*arr[j]):
                count=count+1
                
    return( count)
t=int(input())
while(t>0):
    n= int(input())
    s= input()
    lst = s.split()
    arr = list(map(int,lst))
    print(pair_array_product( n ,arr ))
    t= t-1
