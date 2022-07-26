Weight = input("Enter your weight for it to be converted: ")
Choose = input("(L)bs or (K)g: ")
L = 2*int(Weight)
K = 0.5*int(Weight)

if Choose.upper() == "L":
    print("You are " + str(L) + " Pounds!")
elif Choose.upper() == "K":
    print(f"You are {K} Kilograms!")

#weight = input("What is your weight in pounds? ")
#weighty = int(weight) * 0.45
#print("You are " + str(weighty) + " kilograms")