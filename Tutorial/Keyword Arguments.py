def greet_user1(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')
    print(f'Welcome aboard {first_name} {last_name}')
def calc_cost(total, shipping, discount):
    print(f'I will now mention the total, shipping and discount:{total}, {shipping}, {discount}')
print("Welcome to this coding exercise!") #


#greet_user1("Smith", "John") #Positional Arguments: position matters. This would say "Smith John" but we want "John Smith"

#greet_user1(last_name="Smith", "John") #Use positional arguments first, then keyword argument, otherwise this error occurs

greet_user1("Dylan", last_name="Singhabahu") #These keyword arguments specifies the positions of the name
calc_cost(total=50, shipping=5, discount=0.1) #Idk how to include this into the function
print("Finish")