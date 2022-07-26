a = ">"
while a != "quit": #Or you can use "while True:" where the break serves as the "break" or != which means it stops the loop
    a = input(">").lower() #Makes everything lowercase when inputted

    if a == "start":
        print("Car Started...Ready to go!")
    elif a == "stop":
        print("Car stopped.")
    elif a == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif a == "quit":  # this stops the "I don't understand that" from occuring when typing "quit"
        break
    else:
        print("I don't understand that...")
