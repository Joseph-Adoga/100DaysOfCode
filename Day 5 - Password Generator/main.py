#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for l in range(0, 1):
    letter_random = random.sample(letters, nr_letters)
    # print(letter_random)

for n in range(0, 1):
    number_random = random.sample(numbers, nr_numbers)
    # print(number_random)

for s in range(0, 1):
    symbol_random = random.sample(symbols, nr_symbols)
    # print(symbol_random)

letter_choice = ""
for letter in letter_random:
    letter_choice = letter_choice + letter

number_choice = ""
for number in number_random:
    number_choice = number_choice + number

symbol_choice = ""
for symbol in symbol_random:
    symbol_choice = symbol_choice + symbol

total_password = letter_choice + number_choice + symbol_choice
print(f"Your Generated Password is {total_password}")

list_total_password = list(total_password)
# print(list_total_password)
random.shuffle(list_total_password)
# print(list_total_password)

shuffled_password = ""
for list_password in list_total_password:
    shuffled_password = shuffled_password + list_password
print(f"Shuffled: {shuffled_password}")

#Day 5
#Password Generator
#100DaysOfCode
#Angela Yu
#Joseph Adoga
