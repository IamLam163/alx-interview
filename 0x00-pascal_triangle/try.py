#create no of rows
#create a list to hold rows
#iterate over the rows
#create empty list for columns
#iterate to create columns
#write conditional for columns (start/stop)
#write conditional if step 6 is not fulfilled
#append columns to list
#print list(triangle)

'''
get no of rows
declare the list triangle
iterate over no of row
create empty list ofr columns
iterate to create columns
define condition for columns(start/stop)
define condition if prev condition is not met
append num to column
print list
'''

nrows = 5
triangle = []
for i in range(nrows):
    col = []
    for j in range(i+1):
        if j == 0 or j == i:
            col.append(1)
        else:
            num = triangle[i-1][j-1] + triangle[i-1][j]
            col.append(num)
    triangle.append(col)

for row in triangle:
    print(row)
