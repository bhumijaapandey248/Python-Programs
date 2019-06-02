#https://practice.geeksforgeeks.org/problems/binary-array-sorting/0

def binary_array_sorting( n, arr):
    
    arr.sort()
    for i in arr:
        print(i,end=" ")
    print()

t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    arr = list(map(int,lst))
    binary_array_sorting( n, arr)  
    t = t-1
