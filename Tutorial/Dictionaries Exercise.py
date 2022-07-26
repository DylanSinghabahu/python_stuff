phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "???") + " "
print(output)

# the += adds another value with the variable's value
# and assigns the new value to the variable.

#Example:
# x = 3
# x += 2
# print(x)
#5

