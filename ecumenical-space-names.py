import random

test = True

## KOSMANO PERSONAL NAMES
kosmano_given_names = []
kosmano_surnames = []

## PLANET NAMES
old_place_names = ["Argos", "Salamis", "Ithaka", "Phaistos", "Yekaterinburg", "Knossos", "Athens", "Zakros", "Armeni", "Archanes",
    "Macedon", "Sparta", "Attica", "Caspian", "Matano", "Vostok", "Pangaea", "Amazon", "Columbia", "Yangtze", "Altai", "Lepini",
    "Vecchio", "Volturno", "Metaponto", "Pollino", "Nubia", "Parnassus", "Petra", "Tyre", "Sidon", "Yafa", "Vinland", "Helluland",
    "Markland", "Tiangong", "Jimboomba", "Mareeba", "Ballarat"]
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
    "Eunomia", "Perseus", "Khonsu", "Nanuk", "Hagar"]
mythological_place_names = ["Asgard", "Midgard", "Bifrost", "Jotunheim", "Vanaheim", "Alfheim", "Nidavellir", "Helheim", "Niflheim",
    "Muspelheim", "Ydalir", "Valhalla", "Sessrumnir", "Helgafjell", "Gjoll", "Elvinder", "Garbhodaka", "Naraka", "Patala", "Svarga", "Meru",
    "Lanka", "Takamagahara", "Yomi", "Jigoku", "Duat", "Orun", "Ginen", "Ile-Ife", "Tian", "Diyu", "Tamoanchan", "Tlalocan",
    "Mictlan", "Olympus", "Styx", "Phlegethon", "Cocytus", "Acheron", "Lethe", "Elysium", "Tartarus", "Tir na nOg", "Mag Mell",
    "Emain Ablach", "Hy-Brasil", "Falias", "Gorias", "Findias", "Murias", "Hara Berezaiti", "Garo-Demanae", "Hamistagan", "Chinvat",
    "Irkalla", "Hanan Pacha", "Uku Pacha", "Tawantinsuyu", "Tamu", "Prav", "Yav", "Nav", "Peklo", "Meido", "Rarohenga", "Arcadia",
    "Eden", "Zion", "Nirvana", "Xanadu", "Sheol", "Gehenna", "Purgatory", "Heaven", "Speewah"]
symbol_names = ["Exodus", "Utopia", "Century", "Fortuna", "Pax", "Strenuus", "Maroon", "Refuge", "Sentry", "Serpent", "Widow", "Voyager",
    "Crescent", "Eagle", "Relic", "Hoplos", "Talaria", "Makhaira", "Kopis", "Trident", "Aegis", "Pamyat", "Memory", "Caestus",
    "Invictus", "Temerarus", "Fortis", "Vir", "Pietas", "Aequitas", "Venture", "Prospect", "Horizon", "Watchman", "Tophet",
    "Quyen", "Nhiet Tinh", "Huanle", "Gongren", "Thanh", "Kuijia", "Huihuang", "Sinjeon", "Renxing", "Qi Chui", "Adislal",
    "Xindalu", "Troi", "Phao Dai", "Tenger Bambai", "Hyugeso", "Magan", "Ayaan", "Thabo", "Jenali", "Bongani", "Hirsi", "Zuberi",
    "Masego", "Sizwe", "Ladan", "Jabulile", "Warsame", "Thula", "Qasri", "Chengetai", "Fadziso", "Mzoxolo", "Hoodo", "Liibaan",
    "Roonaan", "Freeland", "Richport", "Rangi", "Pembela", "Maeva", "Harta", "Kesempatan", "Kala", "Hope", "Rahi", "Tenang",
    "Holyfield", "Mahalaga", "Waspada", "Kayamutan", "Ard", "Farah", "Aswat Adida", "Midfa'a", "Miah Mortafi'a", "Wogohna",
    "Dam", "Masheat Allah", "Zekra", "Al-Yad", "Bahr Ennour", "Janna", "El Ein", "Moamen", "Boka' Baeid", "Malek", "Al Akdam",
    "Khaled", "Central", "Axiom", "Vanguard", "Liberty", "Fortune", "Amity", "Grand", "Praxis", "Sentinel", "Reliance",
    "Endeavor", "Ascension", "Stalwart", "Heritage", "Empire", "Venture", "Enterprise", "Cidadela", "Dourado", "Boa Esperanca",
    "Fiel", "Borda Dura", "Paraiso", "Ascensao", "Terra Alegre", "Lembranca", "Alto Torre", "Pacifico", "Monumento", "Helder",
    "Lugar de Paz", "Jeongsang", "Dangye", "Uimu", "Yagsog", "Jibae", "Cheongchija", "Bojeung", "Gamsa", "Ihae", "Junbi",
    "Gwanchalja", "Chul", "Sinnyeom", "Tong-Gwa", "Pangyeol", "Mogjeog", "Pungbu", "Insig", "Pinancheo", "Le Coeur", "Prosperite",
    "Aintza", "Fidele", "Gran Exito", "Beraht", "Amparo", "Bouclier", "Izar", "Honoree", "Mirabelle", "Senen", "Valiente",
    "Filoteu", "Kenza", "Igoa", "Esperance", "Kemena", "Pacifique", "Zeitgeist", "Weltgeist", "Kastellan", "Eintracht", "Weisheit",
    "Demut", "Blauwald", "Wachter", "Entwicklung", "Hochburg", "Entschluss", "Ehrfurcht", "Trutzburg", "Gemut", "Schwerweg",
    "Wahrheit", "Belohnung", "Hochachtung", "Streben", "Zenit", "Mandira", "Sayira", "Asraya", "Sabda", "Javaid", "Vasanta",
    "Harsha", "Prana", "Zafar", "Shan", "Thankam", "Udyama", "Deepcastle", "Muireile", "Fjarran", "Dunkyle", "Vandfald",
    "Wideway", "Siorraidh", "Gryten", "Oceanham", "Orlog", "Helgedom", "Standaktig", "Kestavyys", "Bredt Oye", "Klogt Hjerte",
    "Himinn", "Duncanceld", "Claghbhan", "Samchair", "Khrabrost", "Uspekh", "Seriy", "Stanimir", "Konechno", "Svyatoy", "Kuzma",
    "Istochnik", "Aguya", "Blesk", "Volya", "Pobeda", "Nebo", "Krasota", "Mir"]
hist_figure_names = ["Gagarin", "Grissom", "Hong", "Tereshkova", "Armstrong", "Farinata", "Hawking", "Chandrasekhar", "Schwarzchild",
    "Thorne", "Kepler", "Herschel", "Newton", "Boltzmann", "Hooft", "Veltman", "Feynman", "Yakawa", "Kobayashi", "Masukawa", "Nambu",
    "Sakata", "Strabo", "Volkov", "Dobrovolski", "Komarov", "Patsayev", "Crick", "Darwin", "Franklin", "Keimowitz", "Pauling",
    "Wallace", "Watson", "Euler", "Fermi", "Benning", "Yukawa", "Silva", "Eriksson", "Pytheas", "Zheng He", "Fei Xin", "Ma Huan",
    "Gong Zhen", "Skye", "Santiago", "Yang", "Morgan", "Zakharov", "Godwinson", "Lal", "Svensgaard", "Dawn", "Luttinen", "Wright",
    "Garland", "Ganzorig", "Gauss", "Gaosi", "Bradbury"]

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

## function time!

def oplace_namegen():
    pname = random.choice(old_place_names)
    print(pname)

def nplace_namegen(namelist):
    pname = random.choice(namelist)
    x = random.randint(1,10)
    if x <= 3:
        modname = "New"
    elif x <= 6:
        modname = "Neo"
    elif x <= 8:
        modname = "Nova"
    elif x == 9:
        modname = "Nu"
    elif x == 10:
        modname = "Shin"
    print(modname, pname)

def numplace_namegen(namelist):
    pname = random.choice(namelist)
    x = str(random.randint(2, 9))
    print(pname + "-" + x)

def godplace_namegen():
    pname = random.choice(god_names)
    print(pname)

def mythplace_namegen():
    pname = random.choice(mythological_place_names)
    print(pname)

def splace_namegen():
    pname = random.choice(symbol_names)
    print(pname)

## doing shit time!

print("Welcome to the Ecumenical Space Namer!")
oplace_namegen()
nplace_namegen(old_place_names)
numplace_namegen(old_place_names)
nplace_namegen(combo_names)
numplace_namegen(combo_names)
godplace_namegen()
mythplace_namegen()
splace_namegen()
