import random as rnd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
how_many_letters = int(input("How many letters would you like in your password?\n"))
how_many_symbols = int(input("How many symblos would you like?\n"))
how_many_numbers = int(input("How many numbers would you like?\n"))

#easy level

# password = ""
#
# for char in range(0, how_many_letters):
#     password += rnd.choice(letters)
# for sym in range(0,how_many_symbols):
#     password += rnd.choice(symbols)
# for num in range(0, how_many_numbers):
#     password += rnd.choice(numbers)
#
# print(password)

#hard level

password_list = []
for char in range(0, how_many_letters):
    password_list.append(rnd.choice(letters))
for sym in range(0, how_many_symbols):
    password_list.append(rnd.choice(symbols))
for num in range(0, how_many_numbers):
    password_list.append(rnd.choice(numbers))

rnd.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")