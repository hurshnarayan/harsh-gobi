while True:
    try:
        number = int(input("Enter a postive number: "))
        if number < 0:
            raise ValueError("Negative numbers are not allowed!")
        print(f"You entered: {number}. ")
        break
    except ValueError as e:
        print("Error!!", e)
