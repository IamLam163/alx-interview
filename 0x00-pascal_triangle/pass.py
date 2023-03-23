#define rows
nrows = 5

# create a list to hold the rows
list = []

#iterate over rows
for i in range(nrows):
    col = []
    for j in range(i+1): #columns
        if j == 0 or j == i: #if j is @ start or end
            col.append(1)
        else:
            num = list[i-1][j-1] + list[i-1][j]
            print("this is num:", num)
            col.append(num)
    list.append(col)

for row in list:
    print(row)

