command = ">"
started = False
stopped = False
while True: #Or you can use "while True:" where the break serves as the "break" or != which means it stops the loop
    command = input(">").lower() #Makes everything lowercase when inputted
    if command == "start":
        if started: #This means it's already started, as in other words, "if started = True:"
            print("Car is already started!")
        else: #This means it's "if started = False:" matching the current started variable, which is why it begins the game, where you can start the car
            started = True #sets the variable to started variable to True, so that it can send the next msg
            print("Car has started")
    elif command == "stop":
        if not started: #Works when stopped = True
            print("Car has already stopped!")
        else: #Works when stopped = False
            started = False
            print("Car has stopped!")
    elif command == "help":
            print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "quit":  # this stops the "I don't understand that" from occuring when typing "quit"
        break
    else:
        print("I don't understand that...")

