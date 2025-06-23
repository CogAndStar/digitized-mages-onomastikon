import random

test = True
male_sax_names = ["Jay", "Lewis", "Townsend", "Newton", "Harvey", "Pollux",
    "Melchior", "Providence", "Virgil", "Achilles", "Ammon", "Zebulon",
    "Anders", "Tarleton", "Patrick", "Thaddeus", "Antony", "Cassius", "Absalom",
    "Oceanus", "Ingvar", "Sakarias", "Philomon", "Josef", "Calum", "Balthasar",
    "Caspar", "Jethro", "Elijah", "Leon", "Vilhelm", "Myles", "Hercules", "Piet",
    "Cormac", "Sijmen", "Augustine", "Deucalion", "Malachi", "Pluto", "Castor",
    "Jupiter", "Neptune", "Apollo", "Mars", "Vulcan", "Mercury", "Bacchus", "Julian",
    "Kasper", "Frodrik", "Dilton", "Orion", "Dust", "Ignatius", "William", "Floris",
    "Jan", "Floris-Jan", "Ove", "Arthur", "Charles", "Edmund", "Eugene", "Francis",
    "Frederick", "George", "Henry", "Hugh", "James", "John", "Nicholas", "Peter",
    "Richard", "Robert", "Roger", "Thomas", "William", "Artur", "Carel", "Owain",
    "Frans", "Frederik", "Fredrik", "Jurgen", "Georg", "Hendrikus", "Henning",
    "Hugo", "Jacob", "Johan", "Lars", "Nikolaas", "Nils", "Petrus", "Peder",
    "Rikard", "Rupert", "Rutger", "Tomas", "Wilhelmus", "Bertram", "Reason",
    "Abner", "Nestor", "Harper", "Wesley", "Larry", "Neptunus", "Ulf", "Mercurius",
    "Merkurius", "Coeus", "Crius",  "Hyperion", "Iapetus", "Iapetos", "Japetus",
    "Saturn", "Saturnus", "Benjamin", "Mordecai", "Torvald", "Stuart", "Abraham",
    "Everard", "Maximilian", "Maximiliaan", "Benedict", "Glaucus", "Elias",
    "Hubert", "Ferdinand", "Leonard", "Lennart", "Felix", "Silas", "Raphael",
    "Rafael", "Lorenz", "Ignatz", "Jeralt", "Gilbert", "Janneman", "Lodewijk",
    "Ludde", "Leopold", "Valdemar", "Gregory", "Randolph", "Lambert", "Lammert",
    "Rufus", "Diederik", "Derrick", "Roderick", "Akilles", "Matthias", "Matthew",
    "Matteus", "Ralph", "Gunnar", "Glenn", "Christopher", "Oswald", "Osvald",
    "Godfrey", "Godfried", "Gottfrid", "Erwin", "Charon", "Karon", "Deimos",
    "Phobos", "Enceladus", "Enkelados", "Ganymede", "Ganymedes", "Mimas",
    "Oberon", "Auberon", "Titan", "Triton", "Uranus", "Ouranos", "Uranos", "Albert",
    "Adelbert", "Albertus", "Magnus", "Jasper", "Jesper", "Columba", "Cyprian",
    "Mahershalalhasbaz", "Notwithstanding", "Maybe", "Joseph", "Samuel", "Josiah",
    "Moses", "Adam", "Solomon", "Hezekiah", "Amos", "Ephraim", "Isaac", "Jonas",
    "Be-Courteous", "Safely-on-High", "Fight-the-Good-Fight-of-Faith", "Small-Hope",
    "Humiliation", "Love", "Wrestling", "Mortify", "Kill-Sin", "Credence",
    "Fly-Fornication", "Posthumus", "Vashni", "Tellno", "Increase", "Onesiphorus",
    "Zaphnaphpaaneh", "Epaphroditus", "Michalaliel", "Lamentations", "Pharaoh",
    "Judas-Not-Iscariot", "Tribulation", "Zeal-of-the-Land", "Merciful",
    "Steadfast", "Much-Mercy", "Fear-Not", "Sorry-For-Sin", "No-Merit", "Accepted",
    "Thankful", "More-Fruit", "Faint-Not", "Purify", "Safe-Deliverance",
    "What-God-Will", "Humanity", "Faithful", "Anger", "Wroth", "Unfeigned", "Miracle",
    "Job-Raked-Out-of-the-Ashes", "Ashes", "Called"]
female_sax_names = ["Letitia", "Sienna", "Camellia", "Johanna", "Henrietta",
    "Rainier", "Charlotte", "Adelaide", "Emily", "Augusta", "Kestrel", "Beatrice",
    "Keziah", "Micaiah", "Delilah", "Louise", "Georgia", "Cornelia", "Helena",
    "Thea", "Isobel", "Elvira", "Athene", "Samphias", "Rosetta", "Caroline",
    "Proserpine", "Emily", "Juno", "Ceres", "Venus", "Minerva", "Diana", "Vesta",
    "Poppy", "Sylvia", "Hermelien", "Hermine", "Suzanne", "Belinda", "Marina",
    "Loena", "Zephaniah", "Reinhild", "Fanny", "Sonja", "Edith", "Agnes", "Inez",
    "Alice", "Alicia", "Ann", "Anna", "Anne", "Avice", "Dorothy", "Dorothea",
    "Dorotea", "Edit", "Liesbeth", "Elizabeth", "Lisbet", "Ellen", "Helen", "Emma",
    "Hilda", "Hilde", "Joan", "Janna", "Jonna", "Margaret", "Margaretha", "Margit",
    "Mary", "Mirjam", "Marika", "Matilda", "Mathilda", "Machteld", "Mellany",
    "Petronilla", "Pietronella", "Pernilla", "Sarah", "Sara", "Verity", "Marije",
    "Anne-Marije", "Clarity", "Winter", "Gwendolyn", "Bathsheba", "Theia", "Rhea",
    "Rea", "Rheia", "Themis", "Mnemosyne", "Phoebe", "Phoibe", "Febe", "Tethys",
    "Alexandra", "Constance", "Forbearance", "Innocence", "Darla", "Lilith",
    "Tisiphone", "Lilit", "Tisifone", "Alecto", "Alekto", "Hecate", "Megaera",
    "Megara", "Hekate", "Hecate", "Trivia", "Vainglory", "Claudia", "Livia",
    "Justina", "Lucilla", "Drusilla", "Lucia", "Valeria", "Julia", "Thalia",
    "Petra", "Ingrid", "Anette", "Lysithea", "Leonie", "Monica", "Monika",
    "Patricia", "Anselma", "Judith", "Judit", "Aletheia", "Amalthea", "Amphitrite",
    "Amfitrite", "Aurora", "Callisto", "Kallisto", "Camilla", "Kamilla", "Cybele",
    "Kybele", "Daphne", "Dafne", "Dione", "Diotima", "Doris", "Egeria", "Elara",
    "Elektra", "Electra", "Eunomia", "Euphrosyne", "Eufrosyne", "Europa", "Fortuna",
    "Hebe", "Himalia", "Hygieia", "Hygeia", "Io", "Iris", "Nemesis", "Pallas",
    "Pasiphae", "Pasifae", "Psyche", "Sinope", "Columba", "Notwithstanding",
    "Maybe", "Rebecca", "Hannah", "Deborah", "Huldah", "Abigail", "Rachel",
    "Ruth", "Be-Courteous", "Safely-on-High", "Fight-the-Good-Fight-of-Faith",
    "Small-Hope", "Humiliation", "Kill-Sin", "Mortify", "Fly-Fornication",
    "Repentance", "Damaris", "Achsar", "Aphra", "Renewed", "Rejoice", "Increased",
    "Sin-Deny", "Continent", "Joy-Again", "From-Above", "Hopeful", "Faith-My-Joy",
    "Sense", "Humility", "Clemency", "Mercy", "Truth", "Philadelphia" "Silence",
    "Obedience", "Virtue", "Confidence", "Victory", "Changed", "Abuse-Not",
    "Learn-Wisdom", "Lament", "Handmaid", "My-Sake", "Remember", "Peaceable",
    "Amity"]

male_lat_names = ["Oriol", "Percillier", "Zepherin", "Severin", "Remy", "Juan",
    "Martin", "Juan Martin", "Eliseo", "Cristobal", "Tomas", "Pablo", "Orphat",
    "Jacques", "Francois", "Jacques-Francois", "Ladon", "Leviathan", "Lazare",
    "Longin", "Louis", "Albin", "Corentin", "Dominique", "Estienne", "Nicolas",
    "Baptiste", "Benoit", "Blaise", "Roger", "Miguel", "Guillermo", "Gustave",
    "Axelle", "Rafael", "Aymeric", "Artur", "Arturo", "Carlos", "Edmond", "Edme",
    "Edmundo", "Eugene", "Eugenio", "Yvain", "Francisco", "Frederic", "Federico",
    "Georges", "Jorge", "Henri", "Enrique", "Hugo", "Iago", "Jehan", "Juan",
    "Laurent", "Lorenzo", "Pierre", "Pedro", "Ricardo", "Roberto", "Robert",
    "Rogelio", "Guillaume", "Jupiter", "Neptune", "Neptuno", "Pluton", "Mars",
    "Marte", "Vulcain", "Vulcano", "Apollon", "Apolo", "Mercure", "Mercurio",
    "Bacchus", "Baco", "Ocean", "Oceano", "Ceos", "Crios", "Crio", "Hyperion",
    "Hiperion", "Japet", "Iapetus", "Japeto", "Iapeto", "Saturne", "Saturno",
    "Maximilien", "Maximiliano", "Glaucos", "Glauco", "Hubert", "Ferdinand",
    "Fernando", "Leonard", "Leonardo", "Felix", "Sylvain", "Silvio", "Jose",
    "Raphael", "Alois", "Gilbert", "Cyril", "Luis", "Leopold", "Leopoldo",
    "Gregoire", "Lambert", "Lamberto", "Ciriaco", "Thierry", "Rodrigue", "Rodrigo",
    "Achille", "Aquiles", "Mathias", "Mateo", "Raoul", "Raul", "Gwendal",
    "Christophe", "Oswaldo", "Godofredo", "Caronte", "Caron", "Charon", "Deimos",
    "Fobos", "Phobos", "Encelade", "Encelado", "Ganymede", "Ganimedes", "Mimas",
    "Mimante", "Oberon", "Auberon", "Titan", "Triton", "Urano", "Ouranos", "Aubert",
    "Alberto", "Gaspard", "Gaspar", "Colomba", "Columba", "Cyprien", "Cipriano",
    "Domingo", "Leo", "Leon", "Pascal", "Pascual", "Sylvestre", "Gibert",
    "Benito", "Benedicto", "Teofilacto", "Gregorio", "Hildebrand", "Hildebrando",
    "Honorio", "Honore", "Alexandre", "Alejandro", "Boniface", "Bonifacio",
    "Jean-Baptiste", "Augustin", "Joseph-Marie", "Michel", "Gabriel", "Guy",
    "Florimond", "Charles", "Isaac", "Emmanuel", "Alexandre", "Hector", "Gaston",
    "Balthazard", "Annibal", "Alexis", "Annibal-Alexis", "Balthazard-Annibal-Alexis",
    "Balthazard-Annibal", "Balthazard-Alexis"]
female_lat_names = ["Jeliette", "Ariane", "Pilar", "Polaire", "Eliane", "Ana",
    "Sofia", "Ana Sofia", "Alivienne", "Ghislaine", "Ysabeau", "Elena", "Ofelia",
    "Albine", "Corentine", "Dominique", "Estienette", "Nicole", "Catherine",
    "Marie", "Perenelle", "Suzanne", "Monique", "Susana", "Lavande", "Ines",
    "Alice", "Alicia", "Anne", "Anita", "Avis", "Dorothee", "Dorotea", "Edith",
    "Elisabet", "Isabel", "Helene", "Emma", "Juana", "Jehanne", "Laetitia",
    "Leticia", "Marguerite", "Margot", "Margarita", "Maria", "Miriam", "Manon",
    "Mathilde", "Maude", "Mafalda", "Melanie", "Melania", "Petronille", "Petronila",
    "Sara", "Junon", "Juno", "Ceres", "Minerva", "Minerve", "Diane", "Diana",
    "Venus", "Vesta", "Proserpine", "Theia", "Tea", "Rhea", "Rheia", "Rea", "Themis",
    "Temis", "Mnemosyne", "Mnemosine", "Phebe", "Phoebe", "Febe", "Febea", "Tethys",
    "Tetis", "Octavia", "Angelique", "Lilith", "Lilit", "Tisiphone", "Megere",
    "Alecto", "Tisifone", "Megera", "Hecate", "Trivia", "Claudia", "Livie", "Justina",
    "Justine", "Lucille", "Lucia", "Valeria", "Valerie", "Julia", "Julie", "Thalia",
    "Petra", "Perrine", "Bernadette", "Mercedes", "Annette", "Lysithea", "Leonie",
    "Marianne", "Manuela", "Patricia", "Anselma", "Judith", "Judit", "Alethee",
    "Aleteia", "Amalthee", "Amaltea", "Amphitrite", "Anfitrita", "Aurore", "Aurora",
    "Calisto", "Callisto", "Camille", "Camila", "Cybele", "Cibeles", "Dafne",
    "Daphne", "Dione", "Diotima", "Diotime", "Doris", "Egeria", "Egerie", "Elara",
    "Electra", "Electre", "Eunomie", "Eunomia", "Euphrosyne", "Eufrosina", "Europa",
    "Fortuna", "Hebe", "Heba", "Himalia", "Hygie", "Hygee", "Higia", "Io", "Iris",
    "Nemesis", "Pallas", "Palas", "Palade", "Pasiphae", "Pasifae", "Psyche", "Psique",
    "Sinope", "Colombe", "Columba", "Anunciacion", "Resureccion", "Asuncion",
    "Trinidad", "Michelle", "Gabrielle", "Gabriela", "Miguela", "Claire", "Claude",
    "Claudette"]

sax_surnames = ["Ahern", "Bottles", "Burke", "Desmond", "Garrick", "Koenig", "Roop",
    "Blair", "Wetter", "Byrnes", "Ermendinger", "Irving", "Lovejoy", "Meriwether",
    "Weisbach", "Snow", "Smoot", "Risch", "Wheeler", "Whitefish", "Lake", "Holman",
    "Jenkins", "King", "Lawrence", "Millam", "Twelvetrees", "Waggoner", "Womack",
    "Alcindor", "Kagy", "Daniels", "Dawn", "Blackwood", "Bonkel", "van den Broeke",
    "Pickart", "Varmlanning", "Norberg", "Taggert", "Koenig", "Wogan", "Harkaway",
    "Ashburn", "Fieldwake", "Pyke", "Gordon", "Lloyd", "Graytwig", "Woodbury",
    "Steel", "Smalhart", "Crowe", "Kriek", "Giles", "Eddison", "Diggs",
    "Perkamentus", "Christiansen", "Dunder", "Pisk", "Rasmussen", "Smorhar",
    "Albedil", "Anderling", "Bootsman", "Crane", "Dolleman", "Duffeling",
    "Elsdonk", "Filister", "Griffel", "Jonker", "Krauwel", "Leeflang",
    "Lubbermans", "Pander", "Pippeling", "Stubbe", "Tops", "van Brun", "van Winkle",
    "Vonk", "Wemel", "Wolkenveldt", "Allworthy", "Barlow", "Barnette", "Bell",
    "Blackbird", "Black", "Blaising", "Blishen", "Bridgewater", "Brundrick",
    "Burrows", "Calumny", "Chapman", "Cobblefrost", "Cook", "Cooper", "Dane",
    "Danson", "Darden", "Fink", "Fleming", "Ganderwort", "Gillyfoot", "Godswright",
    "Graves", "Green", "Grimsditch", "Hemmings", "Hicks", "Humphrey", "Jackson",
    "Jernigan", "Kneedander", "Lamb", "Lockhorn", "Marshall", "Middleton",
    "Millay", "Moberly", "Moulton", "Nettum", "Newzer", "Oakley", "Peters", "Poe",
    "Pribble", "Purcell", "Quahog", "Ramsay", "Randolph", "Reynard", "Sayre",
    "Sharp", "Shaw", "Sims", "Singleton", "Skipwith", "Slaughter", "Smackhammer",
    "Spore", "Stone", "Stormalong", "Tanner", "Temper", "Treetops", "Walnut",
    "Wardwart", "Wardwell", "Weatherby", "Webb", "Westley", "Whitelock", "Wilkinson",
    "Williams", "Windwood", "Winthrop", "Wise", "Wolfe", "Worple", "Wythe", "Tolliver",
    "Aster", "Donner", "Fischer", "Fluger", "Gabler", "Harding", "Heidelberger",
    "Heizenbert", "Kirsch", "Muntz", "Perschky", "Pfeiffer", "Pitcher", "Potsdam",
    "Rappaport", "Rhine", "Rosenkranz", "Stoppelwald", "von Sigg", "Weiss",
    "Bryant", "Coleman", "Doyle", "Hackett", "McDermot", "O'Brien", "O'Sullivan",
    "Tander", "Ward", "Aborn", "Beining", "Bister", "Blom", "Dult", "Eggelkam",
    "Fromm", "Gulmedal", "Humlesnurr", "Kroken", "Langballe", "Lie", "Lunekjaer",
    "Wiltersen", "Skuggason", "Abernathy", "Cochran", "Kinkaid", "MacDonald",
    "MacDuff", "McGilliguddy", "Pringle", "Proudfoot", "Rankin", "Shanks",
    "Bolling", "Feboldson", "Sundstrom", "Kenyon", "Droelblossom", "Kampfhund",
    "Broom", "Baskerville", "Beausire", "Coffin", "Crossley", "Drake", "Drinkwater",
    "Fairchild", "French", "Heaviside", "Hooten", "Jenner", "Loveless", "Nix",
    "Omohundro", "Passmore", "Quick", "Reddit", "Shade", "Stringfellow", "Warboys"]
lat_surnames = ["Alvarez", "du Nuit", "Castillo", "Gutierrez de la Concha",
    "Baudet", "Fontaine", "Bonjean", "Irigoyen", "Hernandez", "Rusard", "Nicollier",
    "Montero", "Parra", "Vidal", "de Mola", "Calvo de la Puerta", "Gutierrez",
    "de la Concha", "Calvo", "de la Puerta", "Romero", "Serrano", "Cuenca", "Tasis",
    "Beauregard", "Aguinaldo", "del Pozo", "L'Esperance", "Daigneault",
    "de Costebelle", "Gregoire", "Jeronimo", "Leloup", "Rosier", "Anouilh", "Augur",
    "Badeaux", "Bastarache", "Bataillier", "Baudelaire", "Durand", "Lejeune",
    "Levieux", "Erbier", "Hasteeur", "Maignen", "Ossier", "Parcheminier",
    "Toussaint", "Vautour", "Voland", "Ferrer", "Murri", "Legrasse", "Atilier",
    "Bandrel", "Beauvais", "Bellot", "Blemish", "Bonheur", "Cabot", "de Brisay",
    "de Brouillon", "de Buade", "de Kereon", "de Monic", "de Remy", "de Saffray",
    "de Subercase", "Desjardins", "Despain", "du Perron", "Duvall", "Gargot",
    "Glaipon", "Jauncey", "Le Roi", "Lefebvre", "Legrande", "Londubat", "Lortie",
    "Maugrey", "Montferrat", "Parat", "Phillippeaux", "Picquery", "Roche", "Acerbi",
    "Allocco", "Canon", "Esposito", "Fedele", "Gazza", "Hossas", "Lambini",
    "Paciocco", "Pieri", "Piton", "Silente", "Santangelo", "Stivale", "Amorim",
    "Carneiru", "Caruso", "Filhus", "Lima", "Miraphora", "Aberrucia", "Almeida",
    "Altamirano", "Armenteros", "Baca", "Bastedo", "de la Torre", "de Monroy",
    "de Viverro", "Eliza", "Favila", "Flores", "Gonzales", "Guzman", "Lopez",
    "Menendez", "Montero", "Murrieta", "Picazo", "Procopio", "Reyes", "Ruiz",
    "de Apodaca", "Ruiz de Apodaca", "Solmoro", "Tabella", "Tesifon", "Tolipan",
    "Vazquez", "Canembelli", "Beaubois", "Belleau", "Boncadavre", "Deschouettes",
    "Malcorbeau", "de La Croix", "Leforgeron", "Beaufee", "Bellefils", "Bonflamme",
    "Desfoix", "Malgrange", "du Houx", "Dulieu", "Beauloup", "Bellemaitre",
    "Bonmont", "Despyjons", "Malrue", "le Soleil", "Delabaguette", "Boulanger",
    "Dugua", "de Mons", "de Biencourt", "de Pourtincourt", "de Saint-Just",
    "Amador", "de Salazar", "de Saint-Etienne", "de La Tour", "de Razilly",
    "de Menou", "d'Aulnay", "Denys", "Cosnier", "Le Borgne", "de Belle Isle",
    "Motin", "de Reux", "d'Andigne", "de Grandfontaine", "Flotte", "de la Frediere"]

male_mix_names = male_sax_names + male_lat_names
female_mix_names = female_sax_names + female_lat_names
mix_surnames = sax_surnames + lat_surnames

## function definitions
def saxon_name(gender):
    if gender == "male":
        fname = random.choice(male_sax_names)
    elif gender == "female":
        fname = random.choice(female_sax_names)
    else:
        print("Bad gender argument!")
    rand = random.randint(1, 10)
    if rand == 1:
        lname = random.choice(sax_surnames) + "-" + random.choice(sax_surnames)
    elif rand == 10:
        lname = random.choice(sax_surnames) + " " + random.choice(sax_surnames)
    else:
        lname = random.choice(sax_surnames)
    print(fname, lname)

def latin_name(gender):
    if gender == "male":
        fname = random.choice(male_lat_names)
    elif gender == "female":
        fname = random.choice(female_lat_names)
    else:
        print("Bad gender argument!")
    rand = random.randint(1,6)
    if rand == 1:
        lname = random.choice(lat_surnames) + " y " + random.choice(lat_surnames)
    elif rand == 2:
        lname = random.choice(lat_surnames) + " et " + random.choice(lat_surnames)
    elif rand == 3:
        lname = random.choice(lat_surnames) + " " + random.choice(lat_surnames)
    else:
        lname = random.choice(lat_surnames)
    print(fname, lname)

def mixed_name(gender):
    if gender == "male":
        fname = random.choice(male_mix_names)
    elif gender == "female":
        fname = random.choice(female_mix_names)
    else:
        print("Bad gender argument!")
    rand = random.randint(1,9)
    if rand == 1:
        lname = random.choice(mix_surnames) + " y " + random.choice(mix_surnames)
    elif rand == 2:
        lname = random.choice(mix_surnames) + " et " + random.choice(mix_surnames)
    elif rand == 3:
        lname = random.choice(mix_surnames) + " " + random.choice(mix_surnames)
    elif rand == 4:
        lname = random.choice(mix_surnames) + "-" + random.choice(mix_surnames)
    elif rand == 5:
        lname = random.choice(mix_surnames) + " " + random.choice(mix_surnames)
    elif rand == 6:
        lname = random.choice(mix_surnames) + "-" + random.choice(mix_surnames)
    else:
        lname = random.choice(mix_surnames)
    print(fname, lname)

## operation time!

print("Welcome to the Digitized Mages' Onomastikon!")
while test == True:
    choice = input("Are you looking for a particular name, or a swathe of names? ")
    if choice == "particular" or choice == "swathe":
        test = False
    else:
        print("Improper input! Try typing 'particular' or 'swathe', my friend!")

test = True
while test == True and choice == "particular":
    gender = input("Is your mage male or female? ")
    if gender == "male" or gender == "female":
        test = False
    else:
        print("Improper input! Try again, my friend!")

test = True
while test == True and choice == "particular":
    group = input("Is your mage a Saxon, a Latin, or mixed? ")
    if group == "saxon" or group == "latin" or group == "mixed":
        test = False
    else:
        print("Improper input! Try again, my friend!")

test = True
while test == True:
    number = input("How many names of that ilk would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Improper input! Try again, my friend!")

while number > 0 and choice == "particular":
    if group == "saxon":
        saxon_name(gender)
    elif group == "latin":
        latin_name(gender)
    elif group == "mixed":
        mixed_name(gender)
    else:
        print("Something went wrong!")
    number -= 1

while number > 0 and choice == "swathe":
    x = random.randint(1,2)
    if x == 1:
        gender = "male"
    elif x == 2:
        gender = "female"
    else:
        print ("Something went wrong!")

    y = random.randint(1,3)
    if y == 1:
        saxon_name(gender)
    elif y == 2:
        latin_name(gender)
    elif y == 3:
        mixed_name(gender)
    else:
        print("Something went wrong!")
    number -= 1

print("There you go!")
