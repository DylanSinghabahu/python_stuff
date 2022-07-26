c = [5, 2, 5, 2, 2]
b = "x"
for a in c:
    print(f"{a*b}") #multiples the str by the int
print("-------------")
#The inner iteration, the b variable, is cycled through first
#and multiplied to each iteration of the outer loop
#which is the c variable

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = '' #doesn't clear, since it's outside the inner loop but defines the variable, so that as the inner loop repeats output will always = 0, so that an x is printed for each number listed from the range
    for count in range(x_count): #first time it iterates 5 times, from 0 to 4
        output = output + 'x' #creates one x and then this inner loops repeats 5 times for the first x
    print(output) #prints the x's resulted for each amount of each iteration

print("----------------------")

number = [1, 1, 1, 1, 5]
for x_count in number:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)
