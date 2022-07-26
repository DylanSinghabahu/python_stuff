numbers = [5,3,2,1,34,2,42,2]
numbers.append(22) #inserts a number at the end of the row
print(numbers)
print("---------------------------")

poo = [5,3,2,1,34,2,42,2]
poo.insert(0, 10) #inserts the number (specific index/position, the number)
print(poo)
print("---------------------------")

pee = [5,3,2,1,34,2,42,2]
pee.remove(42) #removes a specific number
print(pee)
print("---------------------------")

nnumbers = [5,3,2,1,34,2,42,2]
nnumbers.clear() #clears the numbers in the lists
print(nnumbers)
print("---------------------------")

nuumbers = [5,3,2,1,34,2,42,2]
nuumbers.pop()
print(nuumbers) #removes the last int/index
print("---------------------------")
row = [5,3,2,1,34,2,42,2]
print(row.index(1)) #finds the index for "1"

print("---------------------------")
#print(row.index(50)) #shows there is no 50
print(50 in numbers) #better alternative as it gives a boolean value, saying its false to that value existing
print("---------------------------")
print(row.count(2)) #counts how many "2's" there are
####################################
print("---------------------------")
row.reverse() #sorts in descending order
print(row)
####################################
print("---------------------------")
row.sort()
print(row) #sorts in ascending order
####################################
print("---------------------------")
row2 = row.copy() #copies the row so you can modify a copy instead of the original
row.append(2)
print(row2)
print(row)
print("---------------------------")

list_example = [1,2,3,1,4,6,4,9,2,9,2,3,2,6,5,7]
list = []
for lists in list_example:
    if lists not in list:
        list.append(lists)
print(list)