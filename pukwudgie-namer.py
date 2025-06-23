import random

test = True

pukwudgie_initials = ["T", "J", "N", "K", "Qu", "F", "D", "Ch", "M", "G", "V"]
pukdwugie_medials = ["t", "j", "n", "ff", "ck", "d", "ch", "m", "vv", "gg"]
pukwudgie_vowels = ["a", "o", "i", "aa", "oo", "ii", "er"]

print("Welcome to the Pukwudgie Namer!")
while test = True:
    number = input("How many names would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Improper input! Try typing an Arabic numeral, pal!")

while number > 0:
    fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
    lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
    print(fname + " " + lname)
    number -= 1

print("There's all your names!")
