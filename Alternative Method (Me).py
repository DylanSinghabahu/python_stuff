command = ">"
started = False
stopped = True
while True: #Or you can use "while True:" where the break serves as the "break" or != which means it stops the loop
    command = input(">").lower() #Makes everything lowercase when inputted
    if command == "start" and started == False:
        print("Car Started...Ready to go!")
        started = True #One equal sign means it's set to True as opposed to checking/working if its True or False
        stopped = False
    elif command == "start" and started == True:
        print("Car has already started!")
    elif command == "stop" and stopped == False:
        print("Car stopped.")
        stopped = True
        started = False
    elif command == "stop" and stopped == True:
        print("Car has already stopped!")
        stopped = True
    elif command == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "quit":  # this stops the "I don't understand that" from occuring when typing "quit"
        break
    else:
        print("I don't understand that...")