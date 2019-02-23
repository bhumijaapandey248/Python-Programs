##data1:100 data2:-54 data3:247 
##sum of all items :293

my_dic={"data1":100,"data2":-54,"data3":247}
sum=0
d={}
for i,j in my_dic.items():
    print(f"{i}:{j}",end=" ")
    sum=sum+j
print(f"\nsum of all items :{sum}")


    
