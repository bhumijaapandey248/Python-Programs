##3.	Write a Python program to match key values in two dictionaries.
##Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
##Expected output: key1: 1 is present in both x and y


dic1={'key1': 1, 'key2': 3, 'key3': 2}
dic2={'key1': 1, 'key2': 2}
for (key,value) in set(dic1.items())&set(dic2.items()):

    print(f"{key}:{value} is present in both x and y")
