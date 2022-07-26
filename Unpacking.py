coordinates = (1,2,3)

#instead of
print(coordinates[1])
print("-------------------")
#we can do
coordinates1 = (1,2,3)
x = coordinates1[0]
y = coordinates1[1]
z = coordinates1[2]
print(y)
print("-------------------")

#However, unpacking is the best way of doing this,
# and works both for tuples and lists:
coordinates2 = (1,2,3)
x, y, z = coordinates2
print(y)
print("-------------------")

coordinates3 = [1,2,3]
x, y, z = coordinates3
print(y)
print("-------------------")