# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_lenght = nr_numbers + nr_letters + nr_symbols
print(f"Length of your password is {password_lenght}")
password = []

# Generating Password
for letter_position in range(password_lenght):
    x = random.randint(0, 51)
    password.append(letters[x])

# Injecting Numbers and symbols
randomize = [random.randint(0, nr_numbers + nr_symbols - 1)]
for y in random:
    position = random.ranint(0, nr_numbers + nr_symbols - 1)
    if y != position and len(randomize) <= (nr_numbers + nr_symbols):
        randomize.append(position)



# injecting numbers and symbols - Trial
# for inject_num in range(nr_numbers):
#     password[random.randint(0, password_lenght -1)] = numbers[random.randint(0, 9)]
# for inject_symbol in range(nr_symbols):
#     password[random.randint(0, password_lenght -1)] = symbols[random.randint(0, 8)]

# printing password
password_str = ""
for elements in password:
    password_str = password_str + elements
print(password_str)


# random.shuffle() function in Python to randomize the position
