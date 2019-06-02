#https://practice.geeksforgeeks.org/problems/sum-of-distinct-elements-1/0

def sum_distinct_elements( n, arr ):
    for i in range(0, n+3):
        sum1 =0
        sum2 = 0
        if (arr[i]==arr[i+1]):
            sum1 = sum1 + arr[i]+arr[i+1]+arr[i+2]
            print(sum1)
    sum2 = sum2 + sum1
    print(sum2)

t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    arr = list(map(int,lst))
    index = sum_distinct_elements( n, arr )
    print(index)
    t = t-1
