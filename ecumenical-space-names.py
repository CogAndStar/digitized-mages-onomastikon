import random

test = True

## KOSMANO PERSONAL NAMES
kosmano_given_names = ["Aluminio", "Amazono", "Amikeco", "Amuro", "Arabidopso", "Argono", "Arĝento", "Belo", "Bramaputro",
    "Celo", "Dediĉo", "Delfinio", "Demokratio", "Dioskoreo", "Egalo", "Ekscelenco", "Elektro", "Fero", "Forto", "Fosforo",
    "Gajo", "Gango", "Glicino", "Gosipio", "Ĝentileco", "Harmonio", "Heliumo", "Heveo", "Hibisko", "Hidrogeno", "Humilo",
    "Integro", "Ipomeo", "Iravadio", "Jangzio", "Jenisejo", "Justo", "Kaketao", "Kalcio", "Kanabo", "Karbono", "Kasajo",
    "Kinkono", "Klemato", "Kobalto", "Kompato", "Kongo", "Kromio", "Kupro", "Kverko", "Leno", "Libero", "Madejro", "Magnezio",
    "Makenzio", "Mangano", "Manioko", "Maranjono", "Mekongo", "Misisipo", "Modero", "Muzo", "Natrio", "Neono", "Nikelo", "Nikotiano",
    "Nitrogeno", "Obo", "Oksigeno", "Orinoko", "Orizo", "Oro", "Papavo", "Parano", "Plateno", "Plezuro", "Potenco", "Praktiko",
    "Prospero", "Puruzo", "Ranunkulo", "Saĝo", "Sankt-Laŭrenco", "Silicio", "Solano", "Solidaro", "Sorgo", "Sulfuro", "Ŝinguo",
    "Taliktro", "Tapajozo", "Teorio", "Titano", "Tokantinso", "Trankvilo", "Tritiko", "Tulipo", "Ukajalo", "Vito", "Zeo"]
kosmano_surnames = ["Adeno", "Ajero", "Akijamo", "Alvarezo", "Artemjevo", "Babo", "Barono", "Berioso", "Birko", "Borisovo",
    "Bunhamo", "Cajo", "Ĉubo", "Ĉario", "Ĉeno", "Davano", "Delenijo", "Dengo", "Devino", "Dojo", "Dominiko", "Dubrovo", "Duglaso",
    "Fariso", "Fedjaevo", "Fuglesango", "Furukavo", "Gersto", "Gezeravĝo", "Gorbunovo", "Grebenkino", "Guio", "Guragĉo",
    "Ĝango", "Ĝiango", "Ĝingo", "Hanso", "Hatavejo", "Hermaŝevsko", "Hirano", "Hoŝido", "Jamakavo", "Jamazako", "Jeo", "Jio",
    "Juvo", "Ĵajo", "Ĵuo", "Kadenjuko", "Kadmano", "Kajpero", "Kanajo", "Kirano", "Kristoforeto", "Kugano", "Kumaro", "Lijuo",
    "Liĵvo", "Lio", "Madavano", "Maezavo", "Menono", "Mogbelijo", "Mogenseno", "Morio", "Moro", "Mukajo", "Murtijo", "Najako",
    "Najiro", "Nespolo", "Noguĉo", "Onisho", "Ovĉinino", "Patvardano", "Permitano", "Pesketo", "Petelino", "Piko", "Platonovo",
    "Ponteso", "Prokopyevo", "Radakriŝnano", "Ramono", "Ravo", "Ruĵikovo", "Sarabajo", "Somanato", "Songo", "Ŝarmo", "Tango",
    "Teterjatnikovo", "Vagnero", "Vakato", "Velo", "Viljamo", "Vitnero", "Vango", "Zibro", "Zubrickijo"]
kosmano_names = kosmano_given_names + kosmano_surnames

## AMERICAN NAMES
american_given_names = ["Maui", "Riley", "Emerson", "Taylor", "Addison", "Pepper", "Cat", "Shelley", "Parris", "Justice", "Presley",
    "Whitney", "Devan", "Shelby", "Tennyson", "Jayme", "Jordin", "Kerry", "McKinley", "Camryn", "Odell", "Remington", "Lee",
    "Britton", "Shannon", "Sawyer", "Tristen", "Esme", "Seven", "Daly", "Indiana", "Kapua", "Hunter", "Hadyn", "Alpha", "Ivory",
    "Emmerson", "Dior", "July", "Hollis", "Merritt", "Merit", "Elliot", "River", "Jaeden", "Sinclair", "Kendall", "Wallis",
    "Elliott", "Raleigh", "Yancy", "Jordan", "Wambli", "Darby", "Kingsley", "Sincere", "Kalei", "Reilly", "Shikoba",
    "Briar", "Sutton", "Awee", "Lindsey", "Mahpiya", "Shae", "Cortney", "Madison", "Lacy", "Shirley", "Iqaluk", "Pitsiulaaq",
    "Makana", "Silver", "Ramsey", "Marley", "Grier", "Lacey", "Devon", "Layne", "Skyler", "Indigo", "Mackenzie", "Jaycee",
    "Arl", "Tayler", "Waverly", "Bellamy", "Braidy", "Meredith", "Ellington", "Emery", "Kelley", "Robbin", "Amery", "Rory",
    "Quincy", "Semaj", "Jelani", "Tarqik", "LaShawn", "Cyan", "Munroe", "Beverly", "Beau", "Joss", "Morgan", "Daley", "Sheridan",
    "Qinnuajuaq", "Jadyn", "Windsor", "Lennon", "Jayden", "Collins", "Wynne", "Keanu", "Ellis", "Moon", "Blythe", "Willoughby",
    "Devyn", "Kalani", "Scout", "Lennox", "Wambdi", "Bowie", "Regan", "Dell", "Quin", "Rylee", "Merlyn", "Quinlan", "Ridley",
    "Reign", "Lake", "Avery", "Brook", "Sloan", "Cary", "Honor", "Kamryn", "Aubrey", "Peyton", "Cove", "Royale", "Everest",
    "Leith", "Art", "Dana", "Selby", "Lindsay", "Ocean", "Auden", "Jae", "Reagan", "D'Arcy", "Kenyatta", "Terry", "Adair",
    "Jaiden", "Winslow", "Fortune", "Harlow", "Armani", "Ora", "Hartley", "Sunny", "Sydney", "Kamari", "Blue", "Alexis", "Keahi",
    "Sunday", "Baylor", "Aston", "Sky", "Marlowe", "Karsyn", "Kaipo", "Shelly", "Storm", "Ripley", "Sage", "Cedar", "Hadley",
    "Kawehi", "Murphy", "Raine", "Kennedy"]
american_surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Beaglehole",
    "Bunny", "Cardy", "Caws", "Godolphin", "Goff", "Hender", "Kneebone", "Liddicoat", "Lower", "Maker", "Menhear", "Nancarrow",
    "Penhollow", "Roach", "Rosewall", "Skyburrow", "Tomes", "Vial", "Wills", "Baskerville", "Beausire", "Coffin", "Crossley",
    "Drake", "Drinkwater", "Fairchild", "French", "Heaviside", "Hooten", "Jenner", "Loveless", "Nix", "Omohundro", "Passmore",
    "Quick", "Redditt", "Shade", "Stringfellow", "Warboys", "Brazil", "Breathnach", "Deady", "Fee", "Flood", "Geddes", "Healy",
    "Heaven", "Lawler", "McKey", "McMorrow", "Moriarty", "Nevin", "Noonan", "O'Gormley", "Power", "Rabbitte", "Seery", "Sharkey",
    "Talley", "Banes", "Blackwood", "Clinkscales", "Cockburn", "Forsyte", "Gall", "Greenlaw", "Hood", "Kinghorn", "Laughland",
    "Maitland", "McBroom", "McFee", "Pennycook", "Porteous", "Reach", "Ripper", "Shankland", "Smiley", "Whitelaw", "Breeze",
    "Cadwallader", "Conway", "Days", "Dee", "Glasscock", "Guild", "Idle", "Kidwell", "March", "Merrix", "Onions", "Penderghast",
    "Price", "Prothero", "Saise", "Tudor", "Upjohn", "Wogan", "Wynne"]
american_names = american_given_names + american_surnames

## EURO NAMES
euro_given_names = []
euro_surnames = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon",
    "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", "Muller", "Schmidt", "Schneider",
    "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann", "Schafer", "Koch", "Bauer", "Richter", "Klein",
    "Wolf", "Schroder", "Neumann", "Schwarz", "Zimmermann", "de Jong", "Jansen", "de Vries", "van den Berg", "van Dijk",
    "Bakker", "Janssen", "Visser", "Smit", "Meijer", "de Boer", "Mulder", "de Groot", "Bos", "Vos", "Peters", "Hendriks",
    "van Leeuwen", "Dekker", "Brouwer", "Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez",
    "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Munoz", "Alvarez", "Romero", "Alonso", "Gutierrez", "Rossi",
    "Russo", "Ferrari", "Esposito", "Colombo", "Bianchi", "Romano", "Ricci", "Gallo", "Dal", "Bruno", "Greco", "Marino",
    "Conti", "Giordano", "Rizzo", "de Luca", "Costa", "Mancini", "Lombardi"]
euro_names = euro_given_names + euro_surnames

## RUSSIAN NAMES
russian_given_names = []
russian_surnames = ["Ivanov", "Smirnov", "Petrov", "Sidorov", "Kuznetsov", "Popov", "Vasiliev", "Sokolov", "Mikhailov", "Novikov",
    "Fyodorov", "Ivanova", "Smirnova", "Petrova", "Sidorova", "Kuznetsova", "Popova", "Vasilieva", "Sokolova", "Mikhailova",
    "Fyodorova", "Morozov", "Morozova", "Volkov", "Volkova", "Alekseev", "Alekseeva", "Lebedev", "Lebedeva", "Semyonov",
    "Semyonova", "Yegorov", "Yegorova", "Pavlov", "Pavlova", "Kozlova", "Kozlov", "Stepanov", "Stepanova", "Nikolaev", "Nikolaeva",
    "Orlov", "Orlova", "Andreev", "Andreeva", "Makarov", "Makarova", "Nikitin", "Nikitina", "Zakharov", "Zakharova", "Solovyov",
    "Solovyova", "Zaitsev", "Zaitseva", "Golubev", "Golubeva", "Vinogradov", "Vinogradova", "Belyaev", "Belyaeva", "Tarasov",
    "Tarasova", "Belov", "Belova", "Komarov", "Komarova", "Kiselyov", "Kiselyova", "Kovalyov", "Kovalyova", "Ilyin", "Ilyina",
    "Gusev", "Guseva", "Titov", "Titova", "Kuzmin", "Kuzmina"]
russian_names = russian_given_names + russian_surnames

## JAPANESE NAMES
japanese_given_names = []
japanese_surnames = ["Akiyama", "Mori", "Mukai", "Wakata", "Doi", "Noguchi", "Hoshide", "Yamazaki", "Furukawa", "Yui",
    "Onishi", "Kanai", "Maezawa", "Hirano", "Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Nakamura", "Kobayashi",
    "Yamamoto", "Kato", "Yoshida", "Yamada", "Sasaki", "Yamaguchi", "Matsumoto", "Inoue", "Kimura", "Shimizu", "Hayashi",
    "Saito", "Nakajima", "Abe", "Ikeda", "Hashimoto", "Ishikawa", "Yamashita", "Ogawa", "Ishii", "Hasegawa", "Goto", "Okada",
    "Kondo", "Maeda", "Fujita", "Kuzunoha", "Endo", "Aoki", "Sakamoto", "Murakami", "Amagami", "Isonokami", "Atsuta", "Dazai",
    "Itsukishima", "Yakumo", "Koshimizu", "Ota", "Kaneko", "Fujii", "Fukuda", "Nishimura", "Miura", "Takeuchi", "Nakagawa"]
japanese_names = japanese_given_names + japanese_surnames

## CHINESE NAMES
chinese_given_names = []
chinese_surnames = []
chinese_names = chinese_given_names + chinese_surnames

## INDIAN NAMES
indian_given_names = []
indian_surnames = []
indian_names = indian_given_names + indian_surnames

## CYBORG NAMES
cyborg_given_names = ["Fulan", "Juan", "Hans", "Jan", "Pepito", "Matti", "Maija", "Max", "Erika", "Xiaoming", "Zhiming", "Chunjiao",
    "Ashok", "Falan", "Tadhg", "Mario", "Taro", "Hanako", "Henk", "Ingrid", "Ola", "Kari", "Folani", "Maria", "Juana", "Anna",
    "Ivan", "Pyotr", "Vasya", "Petar", "Fulano", "Mengano", "Zutano", "Somchai", "Somsri", "Sommai", "John", "Jane", "Joe"]
cyborg_letters = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu",
    "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"]
cyborg_numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

personal_names = kosmano_names + american_names + euro_names + russian_names + japanese_names + chinese_names + indian_names + cyborg_given_names

## NAME GEN FUNCTIONS

def kosmano_namegen():
    fname = random.choice(kosmano_given_names)
    lname1 = random.choice(kosmano_surnames)
    lname2 = random.choice(kosmano_surnames)
    lname = lname1 + "-" + lname2
    print(fname, lname)

def american_namegen():
    fname = random.choice(american_given_names)
    lname = random.choice(american_surnames)
    print(fname, lname)

def cyborg_namegen():
    fname = random.choice(cyborg_given_names)
    lname1 = random.choice(cyborg_letters)
    lname2 = random.choice(cyborg_numbers)
    lname = lname1 + "-" + lname2
    print(fname, lname)


## PLANET NAMES
old_place_names = ["Argos", "Salamis", "Ithaka", "Phaistos", "Yekaterinburg", "Knossos", "Athens", "Zakros", "Armeni", "Archanes",
    "Macedon", "Sparta", "Attica", "Caspian", "Matano", "Vostok", "Pangaea", "Amazon", "Columbia", "Yangtze", "Altai", "Lepini",
    "Vecchio", "Volturno", "Metaponto", "Pollino", "Nubia", "Parnassus", "Petra", "Tyre", "Sidon", "Yafa", "Vinland", "Helluland",
    "Markland", "Tiangong", "Jimboomba", "Mareeba", "Ballarat", "London", "New York", "Beijing", "Hong Kong", "Shanghai", "Sydney",
    "Dubai", "Paris", "Singapore", "Tokyo", "Amsterdam", "Bangkok", "Chicago", "Frankfurt", "Guangzhou", "Istanbul", "Jakarta",
    "Kuala Lumpur", "Los Angeles", "Madrid", "Mexico", "Milan", "Mumbai", "Sao Paulo", "Seoul", "Toronto", "Warsaw", "Berlin",
    "Boston", "Brussels", "Buenos Aires", "Dublin", "Dusseldorf", "Houston", "Johannesburg", "Lisbon", "Luxembourg", "Melbourne",
    "Munich", "New Delhi", "Riyadh", "San Francisco", "Santiago", "Shenzhen", "Stockholm", "Taipei", "Vienna", "Washington",
    "Zurich", "Kyoto", "Manitoulin", "Memphis", "Reykjavik", "Sao Salvador", "Wudangshan", "Varanasi", "Amikejo", "Caloris",
    "Skadi", "Maat", "Denali", "Chomolungma", "Sagarmatha", "Huygens", "Barmingrad", "Mouton", "Hadley", "Rumker", "Olympus",
    "Ascraeus", "Elysium", "Arsia", "Pavonis", "Anseris", "Aeolis", "Rheasilvia", "Ahuna", "Boosaule", "Ionia", "Euboea",
    "Herschel", "Janiculum", "Mithrim", "Doom", "Tenzing", "Piccard", "Wright", "Butler", "Dorothy", "Rembrandt", "Mead",
    "Vredefort", "Chicxulub", "Procellarum", "Imbrium", "Utopia", "Hellas", "Isidis", "Argyre", "Veneneia", "Kerwan", "Yalode",
    "Epigeus", "Valhalla", "Heimdall", "Odysseus", "Evander", "Mamaldi", "Tirawa", "Menrva", "Turgis", "Engelier", "Gerin",
    "Falsaron", "Gertrude", "Sputnik", "Burney", "Ephrata", "Zoar", "Oberlin", "Awra Amba", "Moora Moora", "Auroville",
    "Atarashiki", "Hiruharama", "Maungapohatu", "Parihaka", "Ratana", "Riverside", "Jinwar", "Jansiac", "Longo Mai", "Tvind",
    "Christiania", "Friland", "Svanholm", "Dyssekilde", "Damanhur", "Niederkaufungen", "Zegg", "Free and Real", "Tamera",
    "Life and Labor", "Lacabe", "Brithdir Mawr", "Dial House", "Findhorn", "Frestonia", "Tinker's Bubble", "Stapleton",
    "Whiteway", "Poole's Land", "Yarrow", "Dancing Rabbit", "Dreamtime", "East Wind", "Enright Ridge", "Homestead",
    "Nottingham", "Stelle", "Sunrise", "Sunward", "Tenacious Unicorn", "Trumbullplex", "Bryn Gweled", "Ganas", "Modern Times",
    "Mohegan", "Helicon", "Acorn", "Twin Oaks", "Celo", "Serenbe", "Black Bear", "Drop", "Equality", "Halcyon", "Home", "Kaliflower",
    "Slabs", "Morehouse", "Cecilia", "Las Gaviotas", "New Lanark", "New Harmony", "Brook", "La Reunion", "Silkville", "Corning",
    "Fairhope", "Kaweah", "Llano del Rio", "Los Mochis", "New Australia", "Nevada City", "Oneida", "Ruskin", "Rugby", "Sointula",
    "Arcosanti", "Skaneatales", "Sodus", "Wisconsin", "Clermont", "Alphadelphia", "Kristeen", "Icaria", "Amana", "Raritan",
    "Octagon", "Llewellyn", "Progressive", "Esperanza", "Altruria", "Am Olam", "Nucla", "Bellamy", "Freedom", "Arden", "Freeland",
    "Post", "Free Acres", "New Llano", "Druid", "Kerista", "Uranian", "Jerusalem", "Jericho"]
god_names = ["Odin", "Harbard", "Vak", "Valtaid", "Wodun", "Wotan", "Thor", "Donar", "Frigg", "Frigga", "Freja", "Hel", "Hela", "Baldr",
    "Heimdall", "Sif", "Loki", "Tyr", "Freyja", "Frau", "Freyr", "Skadi", "Njordr", "Urd", "Verdandi", "Skuld", "Agni", "Jataveda", "Kravyada", "Abhimani",
    "Atithi", "Vaisvanara", "Durga", "Devi", "Ganesha", "Ganapati", "Indra", "Devaraja", "Kali", "Bhavatarini", "Karttikeya", "Murugan",
    "Skanda", "Lakshmi", "Parvati", "Sarasvati", "Biancaitian", "Shiva", "Maheshvara", "Nataraja", "Surya", "Savitar", "Varuna", "Suiten",
    "Vishnu", "Jagannatha", "Yamaraja", "Yama", "Yanluowang", "Enma", "Shinje", "Amaterasu", "Tsukiyomi", "Susano-O", "Hachiman", "Inari", "Ama-no-Uzume", "Sarutahiko", "Takemikazuchi", "Ebisu",
    "Okuninushi", "Bishamon", "Benzaiten", "Fukurokuju", "Kisshoten", "Hotei", "Nokomis", "Muzzu-Kumik-Quae", "Winona", "Tekawerahkwa",
    "Maudjee-Kawiss", "Pukawiss", "Jiibayaabooz", "Nanabozho", "Wisakedjak", "Anubis", "Bast", "Hathor", "Horus", "Isis", "Khnum",
    "Osiris", "Ptah", "Ra", "Set", "Sobek", "Thoth", "Eshu", "Legba", "Taiyewo", "Kahinde", "Moremi", "Obatala", "Oduduwa",
    "Ogun", "Orisha-Oko", "Orunmila", "Osanyin", "Oshossi", "Oshun", "Oya", "Shango", "Sonponna", "Yemoja", "Chang'e", "Confucius",
    "Erlang", "Fuxi", "Guan Yu", "Guanyin", "Huangdi", "Laozi", "Nezha", "Nuwa", "Wukong", "Yandi", "Shennong", "Xiwangmu",
    "Chalchihuitlicue", "Chantico", "Chicomecoatl", "Centeotl", "Huehuecoyotl", "Huitzilopochtli", "Itzpapalotl", "Mictecacihuatl",
    "Quetzalcoatl", "Mictlantecuhtli", "Tezcatlipoca", "Tlaloc", "Xipe Totec", "Xochipilli", "Xochiquetzal", "Aengus", "Brigid",
    "Dagda", "Dian Cecht", "Donn", "Goibniu", "Lugh", "Manannan", "Morrigan", "Nuada", "Ogma", "Samedi", "Damballa", "Ezili",
    "Kalfu", "Lasyren", "Anahita", "Ashi", "Atar", "Haoma", "Hvare-Khshaeta", "Mangha", "Mithra", "Rashnu", "Sraosha",
    "Tishtrya", "Vanant", "Vata-Vayu", "Verethragna", "Zam", "Bragi", "Vishvakarman", "Omoikane", "Biboonike", "Wepwawet",
    "Erinle", "Doumu", "Xolotl", "Hecate", "Midir", "Enki", "Enlil", "Ereshkigal", "Ishtar", "Marduk", "Nanshe", "Nergal",
    "Ninhursag", "Ninlil", "Ninurta", "Shamash", "Nanna", "Tammuz", "Tiamat", "Anu", "Chasca", "Coniraya", "Illapa", "Inti",
    "Kuychi", "Mama Cocha", "Mama Killa", "Pachacamac", "Pachamama", "Supay", "Vichama", "Rongomatane", "Lono", "Ono",
    "Rehua", "Tamanuitera", "La", "Laa", "Ra'a", "Tanemahuta", "Kane", "Tane", "Tangaroa", "Kanaloa", "Ta'aroa", "Tagaloa",
    "Tawhirimatea", "Tawhiri", "Tumatauenga", "Tu", "Ku", "Maui", "Pele", "Atagha", "Dayisun", "Erlik", "Geser", "Jayaghaghtsi",
    "Khormusta", "Manakhan", "Perun", "Mokosh", "Jarilo", "Morena", "Veles", "Zhiva", "Svarog", "Dazhbog", "Svarozhich",
    "Radegast", "Zorya", "Belobog", "Chernobog", "Gorgon", "Hydra", "Phoenix", "Artemis", "Proteus", "Nausicaa", "Circe",
    "Hercules", "Theseus", "Borr", "Antaeus", "Cacus", "Dis", "Plutus", "Teshub", "Hebat", "Mnemosyne", "Morana", "Balor",
    "Bres", "Cernunnos", "Elatha", "Fomor", "Partholon", "Surtur", "Sinmara", "Amun", "Sekhmet", "Anhur", "Neith", "Ma-at",
    "Ammut", "Asteria", "Ker", "Triodia", "Yamm", "Tefnut", "Enoch", "Laban", "Mizraim", "Joab", "Goliath", "Clio",
    "Sigurd", "Despoina", "Arion", "Eubolos", "Typhon", "Aita", "Echidna", "Moros", "Alcyoneus", "Themis", "Eirene",
    "Eunomia", "Perseus", "Khonsu", "Nanuk", "Hagar", "Manegarm", "Hugin", "Nidhogg", "Valkyrie", "Thrym", "Jotun", "Goryo"]
mythological_place_names = ["Asgard", "Midgard", "Bifrost", "Jotunheim", "Vanaheim", "Alfheim", "Nidavellir", "Helheim", "Niflheim",
    "Muspelheim", "Ydalir", "Valhalla", "Sessrumnir", "Helgafjell", "Gjoll", "Elvinder", "Garbhodaka", "Naraka", "Patala", "Svarga", "Meru",
    "Lanka", "Takamagahara", "Yomi", "Jigoku", "Duat", "Orun", "Ginen", "Ile-Ife", "Tian", "Diyu", "Tamoanchan", "Tlalocan",
    "Mictlan", "Olympus", "Styx", "Phlegethon", "Cocytus", "Acheron", "Lethe", "Elysium", "Tartarus", "Tir na nOg", "Mag Mell",
    "Emain Ablach", "Hy-Brasil", "Falias", "Gorias", "Findias", "Murias", "Hara Berezaiti", "Garo-Demanae", "Hamistagan", "Chinvat",
    "Irkalla", "Hanan Pacha", "Uku Pacha", "Tawantinsuyu", "Tamu", "Prav", "Yav", "Nav", "Peklo", "Meido", "Rarohenga", "Arcadia",
    "Eden", "Zion", "Nirvana", "Xanadu", "Sheol", "Gehenna", "Purgatory", "Heaven", "Speewah", "Aaru", "Akhet", "Benben", "Arcadia",
    "Asphodel", "Atlantis", "Hyperborea", "Laistrygon", "Meropis", "Nysa", "Oceanus", "Panchaia", "Themiscyra", "Biarmaland",
    "Fositesland", "Hvergelmir", "Kvenland", "Mimisbrunnr", "Norumbega", "Svartalfheim", "Urdarbrunnr", "Te Po", "Ao", "Hawaiki",
    "Agartha", "Amaravati", "Brahmaloka", "Himavanta", "Jambudvipa", "Kailash", "Ketumati", "Kshira Sagara", "Manidvipa",
    "Mayasabha", "Mandara", "Meru", "Nirvana", "Pialral", "Samavasarana", "Sanzu", "Shakadvipa", "Shambhala", "Siddhashila",
    "Tripura", "Trayastrimsa", "Uttarakuru", "Vaikuntha", "Vaitarani", "Fusang", "Kunlun", "Longmen", "Buzhou", "Penglai",
    "Shangri-La", "Shangdu", "Xanadu", "Antillia", "As-Sirat", "Barzakh", "Bethulia", "Hitfun", "Iram", "Jabulqa", "Jabulsa",
    "Kolob", "Malakut", "Matarta", "Pandemonium", "Piriawis", "Pleroma", "Siniawis", "Zarahemla", "Zerzura", "Annwn", "Avalon",
    "Camelot", "Celliwig", "Lyonesse", "Rocabarraigh", "Tech Duinn", "Tir fo Thuinn", "Ys", "Adlivun", "Alatyr", "Al-Wakwak",
    "Aztlan", "Buyan", "Cockaigne", "Domdaniel", "Kitara", "Hubur", "Kalunga", "Opona", "Oponskoye", "Saguenay", "Kitezh",
    "Lemuria", "Lintukoto", "Lukomorye", "Mahoroba", "Mu", "Nibiru", "Onigashima", "Paititi", "Pohjola", "Ryugu", "Summerland",
    "Thule", "Westernesse", "Yomotsu Hirasaka"]
symbol_names = ["Exodus", "Utopia", "Century", "Fortuna", "Pax", "Strenuus", "Maroon", "Refuge", "Sentry", "Serpent", "Widow", "Voyager",
    "Crescent", "Eagle", "Relic", "Hoplos", "Talaria", "Makhaira", "Kopis", "Trident", "Aegis", "Pamyat", "Memory", "Caestus",
    "Invictus", "Temerarus", "Fortis", "Vir", "Pietas", "Aequitas", "Venture", "Prospect", "Horizon", "Watchman", "Harmony",
    "Economy", "Nashoba", "Phalanstery", "Community", "Hope", "Fruit", "Phalanx", "Knowledge", "Crisis", "Fecundity", "Cold",
    "Moisture", "Showers", "Cleverness", "Edge", "Nectar", "Serenity", "Tranquility", "Vapors", "Storms", "Summer", "Autumn",
    "Goodness", "Sorrow", "Excellence", "Happiness", "Joy", "Winter", "Softness", "Luxury", "Death", "Forgetfulness", "Hatred",
    "Perseverance", "Solitude", "Dreams", "Hope", "Time", "Fear", "Spring", "Decay", "Sleep", "Love", "Roughness", "Trust",
    "Honor", "Rainbows", "Center", "Dew", "Success", "Beacon", "Signal", "Pharos", "Haven", "Sanctum", "Shade", "Oscuro", "Atlas",
    "Ohu", "Mistral", "High Garden", "Forest Primeval", "Blackroot", "Greenhouse", "Last Rose of Summer", "Lucky Autumn", "Dreams of Green",
    "Velvetgrass", "Planetsong", "Fallow Time", "Autumn Grove", "Flowers Preach", "Resplendent Oak", "Lily of the Valley",
    "Virgin Soil", "Garden of Paradise", "Thorny Vineyard", "Trees of Wisdom", "Echoing Forests", "Greenwell", "Sun Soaked",
    "Gnarled Roots", "Oaken Shadow", "Blessed Autumn", "Glowmite", "Greenway", "Nature's Bounty", "Mother's Love", "Garden of the Deep",
    "Water Garden", "Ocean Flower", "Falling Water", "Cradle", "Sea of Green", "Dawn", "Edict", "Delight", "Consecration", "Purity",
    "Stigmata", "Well of Souls", "Childhood's End", "Trial By Fire", "Misericordia", "Hermitage", "Flensing", "Rising", "Ark",
    "Reverie", "Science", "Processing", "Flow of Control", "Recursive", "Pseudocode", "Flowchart", "Halting Problem", "Gargoyle Garden",
    "Ergonomia", "Sprawl", "Opticommons", "Stack Heap", "Secret Hollow", "Moonshadow", "Alphaville", "Black Hat", "White Hat",
    "Tears In Rain", "Steelfount", "Common Ground", "Labor Trust", "Worker's Paradise", "Living Standard", "Monkeywrench",
    "Staples of Life", "Hammer and Tongs", "Anvil of Man", "Future's Fulcrum", "Overlords' Despair", "Collective Organization",
    "Union Labor", "Despots' Chagrin", "Collective Bargaining", "Rerum Novarum", "Light and Air", "A La Fumee", "Workers' Rights",
    "Emperors' Misery", "Class Struggle", "Colony", "Zhimindi", "Kolonio", "Hive", "Teeming", "Throng", "Nest", "Den", "Labyrinth",
    "Swarming", "Nexus", "Artery", "Grid", "Collective", "Watcher's Eye", "Huddling of the People", "Fellowship", "Endeavor",
    "People's Endeavor", "Fecundity", "Aspiration", "Serene", "Collective Achievement", "Will's Triumph", "Human Potential",
    "Dauntless", "Camaraderie", "Endurance", "Purpose", "Duty", "Struggle's Respite", "Victory", "Serve the People", "Order's Bulwark",
    "Inner Balance", "Redemption", "Conclave", "Judgement Seat", "Sanctity", "Hallowed", "Revelation", "Great Refuge", "Amnesty",
    "Rights", "Aid", "Settlement", "Health", "Education", "Justice", "Information", "Relief", "Social Progress", "Research",
    "Buran", "Mir", "Relativity", "Discovery", "Gold", "Unity", "Scientific Method", "Singularity", "Transhumanism",
    "Peer Review", "Unified Field", "Zero Point", "Stream of Consciousness", "Serendipity", "Helix", "Aurora", "Genius",
    "Curiosity", "Hypothesis", "Taste of the Fruit", "Strands of Life", "Gravity's Pull"]
hist_figure_names = ["Gagarin", "Grissom", "Hong", "Tereshkova", "Armstrong", "Farinata", "Hawking", "Chandrasekhar", "Schwarzchild",
    "Thorne", "Kepler", "Herschel", "Newton", "Boltzmann", "Hooft", "Veltman", "Feynman", "Yakawa", "Kobayashi", "Masukawa", "Nambu",
    "Sakata", "Strabo", "Volkov", "Dobrovolski", "Komarov", "Patsayev", "Crick", "Darwin", "Franklin", "Keimowitz", "Pauling",
    "Wallace", "Watson", "Euler", "Fermi", "Benning", "Yukawa", "Silva", "Eriksson", "Pytheas", "Zheng He", "Fei Xin", "Ma Huan",
    "Gong Zhen", "Skye", "Santiago", "Yang", "Morgan", "Zakharov", "Godwinson", "Lal", "Svensgaard", "Dawn", "Luttinen", "Wright",
    "Garland", "Ganzorig", "Gauss", "Bradbury", "Faraday", "Roentgen", "Van 't Hoff", "Prudhomme", "Behring", "Dunant", "Passy",
    "Lorentz", "Zeeman", "Fischer", "Ross", "Mommsen", "Ducommun", "Gobat", "Becquerel", "Curie", "Arrhenius", "Bjornson", "Cremer",
    "Finsen", "Rayleigh", "Ramsay", "Pavlov", "Echegaray", "Muir", "Gibson", "Marx", "Engels", "Lenin", "Mao", "Tsiolkovsky",
    "Mendeleev", "Pavlov", "Lomonosov", "Korolev", "Mendel", "Schrodinger", "Owen", "Fourier", "Bellamy"]

combo_names = old_place_names + god_names + mythological_place_names + symbol_names + hist_figure_names

## plant name generation options
## 1. old place name on its own
## 2. old place name w/ "new", "neo", "nu", "nova", "shin", etc. in front of it
## 3. god name
## 4. mythological place name
## 5. symbol name
## 6. given name
## 7. surname
## 8. given name's world
## 9. surname's world
## 10. old place name with -# after it

## planet function time!

def oplace_namegen():
    pname = random.choice(old_place_names)
    print(pname)

def nplace_namegen(namelist):
    pname = random.choice(namelist)
    x = random.randint(1,5)
    if x == 1:
        modname = "New"
    elif x == 2:
        modname = "Neo"
    elif x == 3:
        modname = "Nu"
    elif x == 4:
        modname = "Nova"
    elif x == 5:
        modname = "Shin"
    print(modname, pname)

def numplace_namegen(namelist):
    pname = random.choice(namelist)
    x = random.randint(1,3)
    if x == 1:
        y = str(random.randint(2, 4))
        print(pname + "-" + y)
    elif x == 2:
        y = random.randint(1,5)
        if y == 1:
            modname = "I"
        elif y == 2:
            modname = "II"
        elif y == 3:
            modname = "III"
        elif y == 4:
            modname = "IV"
        elif y == 5:
            modname = "V"
        print(pname, modname)
    elif x == 3:
        modname = "Prime"
        print(pname, modname)

def godplace_namegen():
    pname = random.choice(god_names)
    print(pname)

def mythplace_namegen():
    pname = random.choice(mythological_place_names)
    print(pname)

def splace_namegen():
    pname = random.choice(symbol_names)
    print(pname)

def hplace_namegen():
    pname = random.choice(hist_figure_names)
    print(pname)

def possplace_namegen():
    namesake = random.choice(personal_names)
    x = random.randint(1,2)
    if x == 1:
        pname = namesake
    elif x == 2:
        pname = namesake + "'s World"
    print(pname)

## ultimate mode
def planet_namegen():
    x = random.randint(1,10)
    if x == 1:
        oplace_namegen()
    elif x == 2:
        nplace_namegen(old_place_names)
    elif x == 3:
        nplace_namegen(old_place_names)
    elif x == 4:
        godplace_namegen()
    elif x == 5:
        mythplace_namegen()
    elif x == 6:
        splace_namegen()
    elif x == 7:
        hplace_namegen()
    elif x == 8:
        nplace_namegen(combo_names)
    elif x == 9:
        nplace_namegen(combo_names)
    elif x == 10:
        possplace_namegen()
## doing shit time!

print("Welcome to the Ecumenical Space Namer!")
while test == True:
    choice = input("What kind of name would you like? Options: Kosmano, American, Cyborg, Planet ")
    if choice == "Kosmano" or choice == "American" or choice == "Cyborg" or choice == "Planet":
        test = False
    else:
        print("Error! Please input one of the options, making sure to capitalize the first letter only!")

test = True
while test:
    number = input("How many names would you like? ")
    try:
        number = float(number)
        test = False
    except:
        print("Error! Please input an Arabic numeral.")

while number > 0:
    if choice == "Kosmano":
        kosmano_namegen()
    elif choice == "American":
        american_namegen()
    elif choice == "Cyborg":
        cyborg_namegen()
    elif choice ==  "Planet":
        planet_namegen()
    number -= 1

print("There's all your names.")
