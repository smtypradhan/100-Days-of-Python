
small_l = list(map(chr, range(97, 123)))
capital_l = list(map(chr, range(65, 91)))
letters = small_l + capital_l

numbers = list(map(chr, range(48, 58)))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random 

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)   

# print(password)

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))


for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

    
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")