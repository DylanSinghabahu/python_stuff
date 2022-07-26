temperature = 10
#sets the temperature value into 10, but using two equal signs produce a boolean result

if temperature > 30:
    print("Hot Day")

elif temperature > 10:
    print("Cold Day")

else:
    print("Perfect Temperature!!!")

print("------------------------------")

name = "Dylan"

if len(name) < 3:
    print("Name must be at least 3 characters long")

elif len(name) > 50:
    print("Name can be a maximum of 50 characters long")

else:
    print("Epic name!")
print("------------------------------")

test = 2
print("John " + str(53 - test)) #When to use "str()"