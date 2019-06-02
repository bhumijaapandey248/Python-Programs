##As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar which contains N chocolate squares. Each of the square has a tastiness level which is denoted by an array A[].
##Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first. 
##Determine the tastiness level of the square which his sister gets.
##Input : 
##3
##5
##5 3 1 6 9
##6
##2 6 4 8 1 6
##4
##2 2 2 2
##Output : 
##1
##1
##2



def removeFirst_last( n, arr ):
    for i in arr:
        arr.sort()
    return arr[0]

t = int(input())
while(t>0):
    n = int(input())
    s = input()
    lst = s.split()
    arr = list(map(int,lst))
    index = removeFirst_last( n, arr )
    print(index)
    t=t-1





