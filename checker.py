import re

password = input("Enter password: ")

length = len(password) >= 8
upper = re.search("[A-Z]", password)
lower = re.search("[a-z]", password)
digit = re.search("[0-9]", password)
symbol = re.search("[@#$%^&*!]", password)

if length and upper and lower and digit and symbol:
    print("Strong password")
else:
    print("Weak password")
