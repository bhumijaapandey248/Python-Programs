##1.	Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
##Sample String: 'abc', 'xyz' 
##Expected Result: 'xyc abz'


str1='abc'
str2='xyz'
##s1=str1[0:2]
##s2=str2[-1]
s1=(str1[0:2]+str2[-1])
s2=(str2[0:2]+str1[-1])
print(s1+" "+s2)
