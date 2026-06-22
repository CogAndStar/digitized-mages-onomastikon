import random

test = True

natural_order_adjectives = ["Beloved", "Bitter", "Blessed", "Brave", "Chief", "Compassionate", "Constant", "Desired",
    "Divine", "Earnest", "Famous", "Flowering", "Fortunate", "Free", "Hallowed", "Happy", "Industrious", "Laughing",
    "Loyal", "Manly", "Mighty", "Noble", "Peaceful", "Praiseworthy", "Powerful", "Prayerful", "Protecting", "Pure",
    "Ready", "Sharp", "Shining", "Small", "Strong", "Willful", "Swift", "Valiant", "Victorious", "Warlike", "Wealthy",
    "Wise", "Worthy", "Young", "Living", "Ready", "Long", "Cold", "Wild", "Blue", "Happy", "White", "Twilit", "Black",
    "Beautiful", "Cheerful", "Green", "Nether", "Burning", "Hollow", "Sunken", "Deep", "Bright", "Gray", "Hard",
    "Wakeful", "Scornful", "Gentle", "Pleasant", "Dark", "Brown", "Rich", "Shorn", "Upward", "Daylit", "Sweet",
    "Joyous", "Blissful", "Flaxen", "Broad", "Stiff", "Cruel", "Darling", "Secret", "Middle", "Woven", "Frozen",
    "Good", "Wet", "Friendly", "Crooked", "Lacking", "Spacious", "Helpful", "Whole", "Buried", "Cautious", "Solitary",
    "New", "Rigid", "Singing", "Pale"]
natural_order_nouns = ["Arrow", "Battle", "Brightness", "Counselor", "Crown", "Defender", "Dweller", "Earth", "Farmer",
    "Father", "Fighter", "Forest", "Gift", "Gate", "Giver", "Guardian", "Hammer", "Harvester", "Healer", "Helper",
    "Home", "Horse", "Keeper", "Laurel", "Leader", "Lily", "Lover", "Maid", "Man", "Pearl", "Protector", "Rock",
    "Rose", "Ruler", "Runner", "Smith", "Son", "Stronghold", "Spear", "Staff", "Steward", "Stranger", "Sword",
    "Traveler", "Twin", "Warrior", "Wolf", "Bear", "Eagle", "Lion", "Falcon", "Fox", "Saw", "Hen", "Boar", "Stag",
    "Honey", "Sea", "Power", "Belly", "Rye", "Yew", "Gift", "Fame", "Fern", "Fortune", "Colt", "Pool", "Fen", "Swan",
    "Twilight", "Peace", "Thicket", "Head", "Mud", "Sow", "Servant", "Dye", "Gravel", "Crow", "Beech", "Shepherd",
    "Horn", "Sky", "Keel", "Flint", "Wheat", "Bull", "Grace", "Hawk", "Storm", "Snow", "Bridge", "Road", "Pit", "Lock",
    "Raven", "Mountain", "Hawthorn", "Scorn"]

dragon_syllables = ["ba", "al", "pai", "mon", "bel", "eth", "pur", "son", "as", "mo", "de", "us", "vi", "ne", "ba",
    "lam", "za", "gan", "bel", "i", "al", "am", "du", "si", "as", "a", "gar", "es", "va", "le", "far", "bar", "ba",
    "tos", "gu", "si", "on", "e", "li", "gos", "ze", "par", "ba", "thin", "sa", "le", "os", "aim", "bu", "ne", "ber",
    "ith", "as", "ta", "roth", "fo", "ca", "lor", "ve", "par", "vu", "al", "cro", "cell", "lo", "cer", "al", "mur",
    "mur", "gre", "mo", "ry", "va", "pu", "la", "flau", "ros", "dan", "ta", "li", "on", "vas", "sa", "go", "si", "tri",
    "ip", "os", "ga", "ap", "sto", "las", "o", "ro", "bas", "se", "ir", "ga", "mi", "gin", "aa", "mon", "le", "ra", "je",
    "ne", "bi", "ros", "ro", "no", "ve", "for", "ne", "us", "mar", "cho", "si", "as", "phe", "nex", "sab", "nock", "shax",
    "o", "ri", "ax", "an", "dras", "an", "dre", "al", "phus", "ki", "ma", "ris", "de", "ca", "ra", "bi", "a", "fur", "fur",
    "mal", "thus", "ra", "um", "bi", "frons", "an", "dro", "ma", "li", "us", "fur", "cas", "mar", "bas", "bu", "er",
    "bo", "tis", "mo", "rax", "glas", "ya", "la", "bol", "as", "fo", "ras", "mal", "phas", "haa", "gen", "ti", "ca",
    "mi", "o", "o", "se", "a", "my", "va", "lac"]

def natural_order_gen():
    fname = random.choice(natural_order_adjectives)
    lname = random.choice(natural_order_nouns)
    name = fname + " " + lname
    return name

def dragon_gen():
    x = random.randint(1, 6)
    if x == 1:
        name = random.choice(dragon_syllables) + random.choice(dragon_syllables)
    elif x == 2 or x == 3:
        name = random.choice(dragon_syllables) + random.choice(dragon_syllables) + random.choice(dragon_syllables)
    elif x == 4 or x == 5:
        name = random.choice(dragon_syllables) + random.choice(dragon_syllables) + random.choice(dragon_syllables) + random.choice(dragon_syllables)
    elif x == 6:
        name = random.choice(dragon_syllables) + random.choice(dragon_syllables) + random.choice(dragon_syllables) + random.choice(dragon_syllables) + random.choice(dragon_syllables)
    return name

print("Welcome to Stars Incline Names!")
while test == True:
    namechoice = input("Would you like Natural Order names, or dragon names? ")
    if namechoice != "natural" and namechoice != "dragon":
        print("Improper input! Try typing 'natural' or 'dragon', pal!")
    else:
        test = False

test = True

while test == True:
    number = input("How many names would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Improper input! Try typing an Arabic numeral, pal!")

while number > 0:
    if namechoice == "natural":
        print(natural_order_gen())
    elif namechoice == "dragon":
        print(dragon_gen())
    else:
        print("Something went wrong!")
    number -= 1

print("There's all your names!")
