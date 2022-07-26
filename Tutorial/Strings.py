course = "Python's Course for Beginners" #If using an apostrophe, use double quotes for the string
print(course)
print("--------------------------------")
horse = 'Python Course for "Beginners"' #If using double quotes for quoting, use single quotes for strings
print(horse)
print("--------------------------------")

email = '''
Dear Dylan,

I can type several lines of code,
unlike if I had not used 3 quotes.'''

print(email)
print("--------------------------------")
Example = "Python for Beginners"
print(course[-2]) #Goes backwards from 0, which is P, so we get r
print("--------------------------------")
print(course[0:3]) #Basically a range, which shows the index from 0-3 exlcuding 3, since 0 is counted as the first letter
print("--------------------------------")
print(course[:]) #Returns all the characters

print("Exercise")
name = "Jennifer"
print(name[1:-1]) #This should give letters from e --> e, since the negative is excluded