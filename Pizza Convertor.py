print("Hi and welcome to the social distance Pizza shop.\n" +
      "What sort of pizza would you like?\n" +
      "1. Vegetarian\n" +
      "2. Too Much Meat\n" +
      "3. Scarparella\n" +
      "Enter the number of your selection: ")

selection = int(input())

print("You selected the ", end="") #Ends the line with nothing, instead of the default where a new line is made

if selection == 1:
    print("Vegetarian", end="")
elif selection == 2:
    print("Too Much Meat", end="")
elif selection == 3:
    print("Scarparella", end="")
else:
    print("Secret Mystery", end="")

print(" pizza. Hope you like it, there's no going back because we haven't done loops yet!")
