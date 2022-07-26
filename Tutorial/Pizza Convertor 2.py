pizzas = ["Vegetarian", "Too Much Meat", "Scarparella"]

print("Hi and welcome to the social distance Pizza shop.\n" +
      "What sort of pizza would you like?\n" +
      "1. " + pizzas[0] + "\n" +
      "2. " + pizzas[1] + "\n" +
      "3. " + pizzas[2] + "\n" +
      "Enter the number of your selection: ")

selection = int(input())

print("You selected the ", end="")

if selection >= 1 and selection <= 3:
    print(pizzas[selection - 1], end="")
else:
    print("Secret Mystery", end="")

print(" pizza. Hope you like it, there's no going back because we haven't done loops yet!")
