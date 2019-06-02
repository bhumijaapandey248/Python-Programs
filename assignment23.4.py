##https://practice.geeksforgeeks.org/problems/greater-on-right-side/0
n= int(input())
s = input()
lst = s.split()
arr = list(map(int,lst))

for i in range(1,n-1):
    if(arr[i]<arr[i+1]):
        print(arr[i+1],end=" ")
    elif(arr[i]>arr[i+1]):
        print(arr[i],end=" ")
##    print(arr[i],end=" ")
print(-1)

##17 5 5 5 2 -1

##6
##16 17 4 3 5 2
##17 5 -1

