guess_count = 3
a = 0
the_number = 5
while a < guess_count:
    a+=1
    guess = int(input("Guess Here:"))
    if the_number == guess:
        print("Well Done!")
        break
else:
    print("You've failed!")