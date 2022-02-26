import random
import string


print("Random Password Generator")
print("=========================")

length = int(input("Enter the length of password required: "))

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
number = string.digits
symbols = string.punctuation
all = lowerCase + upperCase + number

includeSymbols = input("Should the password inculde special characters? Please answer yes or no >")

if includeSymbols == "yes":
    all = all + symbols

tempass = random.sample(all, length)

password = "".join(tempass)

print(password)

input("Press any key to close...")
