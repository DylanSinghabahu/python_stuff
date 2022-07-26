try:
    age = int(input("What is your age:"))
    income = 20
    risk = income/age
    print(age)
except:
    print("Invalid Input")
    ##########  DIFFERENT SPECIFIC TYPES OF ERRORS  #############
# except ZeroDivisionError as eerr: #For Division Errors like dividing by 0. The "as err" mentions the specific error
    # print(eerr)
# except ValueError: #if there is an exit code > 0 / if there's an error, this will be printed
    #print("pp")