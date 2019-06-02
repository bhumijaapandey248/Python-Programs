#https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product/0

def minimize_sum( n, arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    p=0
    for i,j in zip(arr1,arr2):
        p=p+(i*j)
    return p
        
t = int(input())
while(t>0):
    n = int(input())
    s1 = input()
    lst1 = s1.split()
    arr1 = list(map(int,lst1))
    s2 = input()
    lst2 = s2.split()
    arr2 = list(map(int,lst2))
    index = minimize_sum( n, arr1, arr2)
    print(index)
    t = t-1
