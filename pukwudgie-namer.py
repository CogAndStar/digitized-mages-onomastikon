import random

test = True

pukwudgie_initials = ["T", "T", "J", "J", "N", "K", "F", "D", "Ch", "M", "G", "V"]
pukwudgie_medials = ["t", "j", "n", "n", "ff", "ff", "ck", "ck", "d", "ch", "m", "v", "g"]
pukwudgie_vowels = ["a", "o", "i", "e", "a", "o", "i", "e", "oo", "ee"]
pukwudgie_finals = ["r", "r", "l", "m", "n"]

## function definitions
def forename_gen():
    x = random.randint(1,3)
    if x == 3:
        fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_finals)
    else:
        fname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
    return fname

def surname_gen():
    x = random.randint(1,3)
    if x == 3:
        lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_finals)
    else:
        lname = random.choice(pukwudgie_initials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels) + random.choice(pukwudgie_medials) + random.choice(pukwudgie_vowels)
    return lname

## operation time!

print("Welcome to the Pukwudgie Namer!")
while test == True:
    namechoice = input("Would you like forenames, surnames, or both? ")
    if namechoice != "forenames" and namechoice != "surnames" and namechoice != "both":
        print("Improper input! Try typing 'forenames', 'surnames', or 'both', pal!")
    else:
        test = False

if namechoice == "forenames":
    lname = input("Please enter your placeholder surname: ")
if namechoice == "surnames":
    fname = input("Please enter your placeholder forename: ")

test = True

while test == True:
    number = input("How many names would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Improper input! Try typing an Arabic numeral, pal!")

while number > 0:
    if namechoice == "forenames":
        print(forename_gen() + " " + lname)
    elif namechoice == "surnames":
        print(fname + " " + surname_gen())
    elif namechoice == "both":
        print(forename_gen() + " " + surname_gen())
    else:
        print("Something went wrong!")
    number -= 1

print("There's all your names!")
