class OtherException(Exception):
    pass


def cause_problems():
    raise OtherException("The cause_problems function caused problems.")


try:
    cause_problems()
    print("Only gets here if no exception turns up earlier")
except OtherException:
    print("Can't fix this one")
except Exception as e:
    print("Now we should fix something")
