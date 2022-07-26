high_income = True
good_credit = False

if high_income and good_credit: #Both statements must be true for eligibility
    print("Eligible for loan 1")

if high_income or good_credit: #At least one statements must be true for eligibility
    print("Eligible for loan 2")

