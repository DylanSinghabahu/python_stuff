matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1] = 20 #modifies the matrix value
print(matrix[0][1])

print("-------------")
epic_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in epic_matrix:
    for items in row:
        print(items)