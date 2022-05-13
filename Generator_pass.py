import random  #This will generate data types randomly.

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #uppercase strings
lowercase_letters = uppercase_letters.lower() #Lowercase strings
digits = "0123456789" #Numerical data
symbols = "()[]{};,:.=/\\*+-_?#"  # Special characters

upper, lower, nums, syms = True, True, True, True  # Set all the data types as true

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all +=digits

if syms:
    all += symbols

lenght = 20
amount = 12

for x in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)