def main():
	arr = list(map(int,input().split()))
	for ele in arr:
		odd_sum = sum_odd_digits(ele)
		print(odd_sum, end=" ")

def sum_odd_digits(n):
    sum = 0
    while(n!=0):
        r=n%10
        if (r%2!=0):            # You have made the program for even but you have to make for odd
            sum=sum+r
        n=n//10
    return sum

if __name__ == '__main__':
	main()
	
