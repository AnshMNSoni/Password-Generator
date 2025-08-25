import random

print("Welcome to the PyPassword Generator!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

symbols = ['@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '/', '?', '|', '\\', ':', ';', '~', '`', '{', '}', '[', ']', '.']

alpha1 = list(map(chr, range(97, 123)))
alpha2 = list(map(chr, range(65, 91)))
alpha = alpha1 + alpha2

letter = int(input("How many letters would you like to have in your password?\n"))
sym = int(input("How many symbols would like you like?\n"))
num = int(input("How many numbers would you like?\n"))

password = []

for ch in range(1, letter + 1):
    password.append(random.choice(alpha))

for sy in range(1, sym + 1):
    password.append(random.choice(symbols))

for i in range(1, num + 1):
    password.append(random.choice(numbers))
    
random.shuffle(password)

final = ""
for item in password:
    final += str(item) 
    
print(f"Your Password is: {final}")