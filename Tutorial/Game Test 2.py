secret_word = "bobs"
guesses = ""
guess_limit = 3
guess_count = 0

while guesses!=secret_word:
    if guess_count < guess_limit:

        guess_count += 1 #Hard mode: Limited tries
        guesses = input("Your Guess:")
        if guesses == secret_word:
            print("Good job, you did it!")
            break
        else:
            print("Try again!")
    else:
        print("You lose")
        break