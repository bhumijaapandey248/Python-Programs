## Perfect Number
## 6

##n=int(input())
##sum=0
##for i in range(1,n):
##    if(n%i==0):
##        sum=sum+i
##if(sum==n):
##    print("It is perfect number !!")
##else:
##    print("It is not perfect number !!")
##
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(n==sum):
        print("It is perfect number !!")
    else:
        print("It is not perfect number !!")
    
num=int(input("number :"))
perfect_number(num)
