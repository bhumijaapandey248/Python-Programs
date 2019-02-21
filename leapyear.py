year=int(input("Enter the year :"))
##if(year%4==0 and year%100!=0):
    
##    print("This Year is leap year !!")
if (year%4==0 or year%400==0) and (year%100!=0):
    
    print("This Year is leap year !!")
else:
    
    print("This Year is not leap year !!")
