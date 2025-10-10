import random

test = True

drasyllic_initials = ["d", "b", "g", "p", "t", "c", "s", "z"]
drasyllic_glides = ["r", "l", "v"]
drasyllic_vowels = ["a", "y", "i", "e", "o", "u"]
drasyllic_finals = ["l", "c", "r", "s", "z"]

def drasyllic_sylgen():
    z = random.randint(1, 6)
    if z <= 5:
        initial = random.choice(drasyllic_initials)
    else:
        initial = ""

    x = random.randint(1, 6)
    if x <= 2 or initial == "":
        glide = random.choice(drasyllic_glides)
    else:
        glide = ""

    vowel = random.choice(drasyllic_vowels)

    y = random.randint(1, 4)
    if x <= 3:
        final = random.choice(drasyllic_finals)
    else:
        final = ""

    syllable = initial + glide + vowel + final
    return syllable

def drasyllic_namegen():
    name1 = drasyllic_sylgen()
    name2 = drasyllic_sylgen()
    name1 = name1.capitalize()
    name2 = name2.capitalize()
    print(name1, name2)

kospos_initials = ["k", "p", "t", "q", "r"]
kospos_vowels = ["a", "e", "u", "o", "eu", "ou", "ae", "au"]
kospos_finals = ["s", "n"]

def kospos_sylgen():
    x = random.randint(1, 6)
    if x <= 5:
        initial = random.choice(kospos_initials)
    else:
        initial = ""

    vowel = random.choice(kospos_vowels)

    y = random.randint(1, 4)
    if x <= 2:
        final = random.choice(kospos_finals)
    else:
        final = ""

    syllable = initial + vowel + final
    return syllable

def kospos_namegen():
    x = random.randint(2, 4)
    name1 = ""
    while x:
        syl = kospos_sylgen()
        name1 = name1 + syl
        x -= 1
    name1 = name1.capitalize()

    y = random.randint(1, 3)
    name2 = ""
    while y:
        syl = kospos_sylgen()
        name2 = name2 + syl
        y -= 1
    name2 = name2.capitalize()

    z = random.randint(1,2)
    name3 = ""
    while z:
        syl = kospos_sylgen()
        name3 = name3 + syl
        z -= 1
    name3 = name3.capitalize()
    name3 = "tou-" + name3

    print(name1, name2, name3)

zasitur_initials = ["z", "s", "t", "d", "p", "b"]
zasitur_vowels = ["a", "i", "u", "aa", "ii", "uu"]
zasitur_finals = ["r"]

def zasitur_sylgen():
    initial = random.choice(zasitur_initials)

    vowel = random.choice(zasitur_vowels)

    x = random.randint(1, 6)
    if x == 1:
        final = random.choice(zasitur_finals)
    else:
        final = ""

    syllable = initial + vowel + final
    return syllable

def zasitur_namegen():
    x = 3
    name = ""
    while x:
        syl = zasitur_sylgen()
        name = name + syl
        x -= 1
    name = name.capitalize()
    print(name)

print("Welcome to the Ygg Name Generator!")
while test == True:
    choice = input("""What kind of ygg name would you like?
    The options are:
    -Drasyllic
    -Kospos
    -Zasitur
    """)
    if choice == "Drasyllic" or "Kospos" or "Zasitur":
        test = False
    else:
        print("Improper input! Make sure you're spelling and capitalizing correctly.")

test = True
while test == True:
    number = input("How many names would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Improper input! Try typing an Arabic numeral.")

while number > 0:
    if choice == "Drasyllic":
        drasyllic_namegen()
    elif choice == "Kospos":
        kospos_namegen()
    elif choice == "Zasitur":
        zasitur_namegen()
    else:
        print("Something went wrong!")
    number -= 1

print("There's all your names!")
