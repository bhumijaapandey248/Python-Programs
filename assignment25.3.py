#https://practice.geeksforgeeks.org/problems/total-distance-travelled-in-an-array/0

def total_distance_travelled( n, arr ):
    count1 =0
    count2 = 0
    for i in range(1,n):
        count1 = count1 + 1
    print(count1)

    for i in range(1,n):
        if (arr[i]!=1):
            count2 = count2 + 1
    print(count2)
    tot_sum = count1 + count2
    return tot_sum
t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    arr = list(map(int,lst))
    index = total_distance_travelled( n, arr )
    print(index)
    t = t-1
