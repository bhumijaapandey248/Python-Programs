#https://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1

def replace_zeroswith_five( n ):
    while(n!=0):
        r = n%10
        if(r==0):
            print('5')
            
        n= n//10
        print(n)
##            n = n/10
##            print(n)
        
##    print(n)

n= int(input())
print(replace_zeroswith_five( n ))
