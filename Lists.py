names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
names[0] = 'Jon' #Changes the first item, in case you made a mistake
print(names)
print(names[2])
print(names[-1])
print(names[2:])
print()

numbers = [1, 4, 5, 2, 7, 9, 20]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)