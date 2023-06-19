#Autho: Jeury Santos
#Title: Password-Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Obtain random letters
final_list= []
for char in range (1, nr_letters + 1 ):
  randon_letter = random.choice(letters)
  final_list += randon_letter

#Obtain random symbols
for i in range (1, nr_symbols +1 ):
  random_sys = random.choice(symbols)
  final_list+= random_sys

#Obtain random numbers
for s in range (1, nr_numbers +1):
  random_n = random.choice(numbers)
  final_list += random_n
#Using the function to shuffle the list and get a char combination
random.shuffle(final_list)

password =""

# a loop to obtain one formart password. 
for char in final_list:
  password += char

print(password)
