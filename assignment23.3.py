##https://practice.geeksforgeeks.org/problems/find-number-of-numbers/1




def count_number(n,k):
    count=0
    while(n!=0):
        r=n%10
        n=n//10
        if(r==k):
            count=count+1
    return(count)
t=int(input())
while(t>0):
    n=int(input())
    s= input()
    lst = s.split()
    arr = list(map(int,lst))
    k= int(input())
    count=0
    for i in range(0,n):
        c =count_number(arr[i],k)
        count=count+c
    print(count)
    t=t-1

##def count_number(n,k):
##    count=0
##    while(n!=0):
##        r=n%10
##        n=n//10
##        if(r==k):
##            count=count+1
##    return(count)
##num(arr, n, k):
##    count=0
##    for i in range(0,n):
##        c =count_number(arr[i],k)
##        count=count+c
##    return count


