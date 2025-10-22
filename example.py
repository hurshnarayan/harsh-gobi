
def isRaining():
    # return bool(int(input("Is it raining. Enter '1' if yes and '0' if no: ")))
    while True:
        try:
            value = int(input("Is it raining? Enter '1' for yes and '0' for no: "))
            if value in (0, 1):
                return bool(value)
            else:
                print("Please enter only 0 or 1.")
        except ValueError:
            print("Invalid input! Please enter a number (0 or 1).")



def haveUmbrella():
    # return bool(int(input("Have umbrella? Enter '1' if true and '0' if no: ")))
    while True:
        try:
            value = int(input("Do you have an umbrella? Enter '1' for yes and '0' for no: "))
            if value in (0, 1):
                return bool(value)
            else:
                print("Please enter only 0 or 1.")
        except ValueError:
            print("Invalid input! Please enter a number (0 or 1).")



if isRaining():
    if haveUmbrella():
        print("Go outside.")
    else:
        while True:
            print("Wait a while")
            if not isRaining():
                print("Go outside")
                break

else:
    print("Go outside")
