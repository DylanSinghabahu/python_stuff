def square(number):
    return number*number

result = square(3)
print(result)

##################################

def triangle(number):
    return number*number

print(triangle(3))


##### Without the return value, the default value returned is "None" #####
def squared(number):
    print(number*number)

print(squared(3))