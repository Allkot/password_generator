import random


password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_gen = ""

password_lengh = int(input("how many symbols in password you need from 8 to 32"))
for symbol in range(password_lengh):
    password_gen += random.choice(password)
print(password_gen)