course = 'Python for Beginners'
print(len(course))
#Function belongs to an object or something else, it is called a method
#For example, course.upper() is a method as it is specific to strings
print("--------------------------------")

print(course.upper()) #Changes to upper-case
print(course.lower()) #Changes to lower-case
print(course.find('o')) #Shows the index for o
print(course.find('Beginners')) #Shows the index for which the word begins
print(course.replace("Beginners","Poo")) #Replaces the word "Beginners" with "Poo." Works the same with letters
print('Python' in course) #Checks/Finds if the word "Python" is in the course variable, using a boolean result
print(course.title()) #Capitalises each word
print(course) #See the difference from title
