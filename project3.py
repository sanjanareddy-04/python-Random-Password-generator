import random

length = int(input("Enter password length: "))

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

for i in range(length):
    password += random.choice(chars)

print("Password:", password)