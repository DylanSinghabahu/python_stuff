def calculator(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(calculator(2, 3))


print("###################################")

def greet_user():
    print('Hi there!') #then it prints the ones below it
    print('Welcome aboard') #except what it started from


print("Start")  # starts here
greet_user()   # calls the greet function jumping to "Hi There!"
print("Finish")
print("--------------------------")


def greet_user1(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')  # then it prints the ones below it
    print(f'Welcome aboard {first_name} {last_name}')  # except what it started from


print("Start")  # starts here
greet_user1("John", "Smith")  # calls the greet function jumping to "Hi There!"
greet_user1("Mary", "Jenkins")  # -->With this function we can pass the information to now say Mary, instead of just printing messages again
print("Finish")

# parameters --> the placeholders of information in functions to RECEIVE information. Like (name) in line 10
# arguments --> the actual pieces of information SUPPLIED to the functions. Like "John" in Line 16
