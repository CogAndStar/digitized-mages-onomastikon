import random

test = True

pukwudgie_initials = ["T", "J", "N", "K", "Kw", "F", "D", "Ch", "M", "G", "V"]
pukwudgie_medials = ["t", "j", "n", "ff", "ck", "d", "ch", "m", "v", "g"]
pukwudgie_vowels = ["a", "o", "i", "a", "e", "e", "o", "i", "oo", "ee"]
pukwudgie_finals = ["r", "l", "m", "n"]

print("Welcome to the Pukwudgie Namer!")
while test == True:
    number = input("How many names would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Improper input! Try typing an Arabic numeral, pal!")

while number > 0:
    x = random.randint(1,6)
    if x == 1 or x == 2 or x == 3:
        fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
        lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
    if x == 4:
        fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_finals)
        lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
    if x == 5:
        fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
        lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_finals)
    if x == 6:
        fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_finals)
        lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_finals)
    print(fname + " " + lname)
    number -= 1

print("There's all your names!")
