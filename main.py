# even_nos = []
# total = 0

# while len(even_nos) < 5:
#     try:
#         number = int(input("Enter a number: "))
#     except ValueError:
#         print("Enter a valid number!!")
#         continue

#     if number % 2 == 0:
#         even_nos.append(number)
#     else:
#         print(f"{number} is odd, try again!")

# total = sum(even_nos)
# print(f"The sum of even nos. {', '.join(map(str, even_nos))} is: {total}")



# even_nos = []
# total = 0

# while len(even_nos) < 5:
#     # try:
#     number = int(input("Enter a number: "))
#     # except ValueError:
#     #     print("Enter a valid number!!")
#     #     continue

#     if number % 2 == 0:
#         even_nos.append(number)
#     else:
#         print(f"{number} is odd, try again!")

# total = sum(even_nos)
# print(f"The sum of even nos. {', '.join(map(str, even_nos))} is: {total}")


# Function to add subtract, multiple divide




def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(subtract(2, 3))
