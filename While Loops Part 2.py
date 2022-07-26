secret_number = 9
a = 0 #Amount of guesses, which can be renamed using shift+f6
guess_limit = 3
while a < guess_limit: #Loop occurs WHILE a is less than the "guess_limit," which is 3. Also prints the following as it loops
    guess = int(input("Guess: ")) #Creates a variable and asks for a guess
    a += 1
    if guess == secret_number: #Variable created = secret number
        print("You won!") #which results in this msg
        break #Stops the loop after guessing correctly. Also the indents are done so it is a part of the while command, otherwise it won't work
else:
        print("You have failed") #Not a part of the while command, since it would send this message after every wrong guess