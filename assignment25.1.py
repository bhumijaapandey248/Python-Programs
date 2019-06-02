#https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum/0

def multiply_left_right_sum( n, arr ):
    n1 = n//2
    for i in arr:
        
        n2 = n%2
        if(n2==0):
##        print(n1)
            sum1 =0
            for i in range(0,n1):
                sum1 = sum1 + arr[i]
##            print(sum1)
            sum2 = 0
            for j in range(n1,n):
                sum2 = sum2 + arr[j]
##            print(sum2)
            res = sum1 * sum2
            return res
        else:
            sum1 = 0
            for i in range(0,n1):
                sum1 = sum1 + arr[i]
##            print(sum1)
            sum2 = 0
            for j in range(n1,n):
                sum2 = sum2 + arr[j]
##            print(sum2)
            res = sum1 * sum2
            return res

t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    arr = list(map(int,lst))
    index = multiply_left_right_sum( n, arr )
    print(index)
    t = t-1
