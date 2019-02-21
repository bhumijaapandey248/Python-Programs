##row :3
##column :4
##enter in row 1 column 1
##2
##enter in row 1 column 2
##4
##enter in row 1 column 3
##6
##enter in row 1 column 4
##1
##enter in row 2 column 1
##9
##enter in row 2 column 2
##0
##enter in row 2 column 3
##2
##enter in row 2 column 4
##5
##enter in row 3 column 1
##6
##enter in row 3 column 2
##2
##enter in row 3 column 3
##9
##enter in row 3 column 4
##7
##[[2, 4, 6, 1], [9, 0, 2, 5], [6, 2, 9, 7]]
##>>> 


r=int(input("row :"))
c=int(input("column :"))
mat=[]

for i in range(0,r):
    mat.append([])
    
for i in range(0,r):
    for j in range(0,c):
        mat[i].append(j)
        mat[i][j]=0

for i in range(0,r):
    for j in range(0,c):
        print("enter in row",i+1,"column",j+1)
        mat[i][j]=int(input())

print(mat)



