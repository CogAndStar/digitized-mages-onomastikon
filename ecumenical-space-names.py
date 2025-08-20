import random

## KOSMANO PERSONAL NAMES
kosmano_given_names = []
kosmano_surnames = []

## PLANET NAMES
old_place_names = []
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
    "Ninhursag", "Ninlil", "Ninurta", "Shamash", "Nanna", "Tammuz", "Tiamat", ]
mythological_place_names = ["Asgard", "Midgard", "Bifrost", "Jotunheim", "Vanaheim", "Alfheim", "Nidavellir", "Helheim", "Niflheim",
    "Muspelheim", "Ydalir", "Valhalla", "Sessrumnir", "Helgafjell", "Gjoll", "Elvinder", "Garbhodaka", "Naraka", "Patala", "Svarga", "Meru",
    "Lanka", "Takamagahara", "Yomi", "Jigoku", "Duat", "Orun", "Ginen", "Ile-Ife", "Tian", "Diyu", "Tamoanchan", "Tlalocan",
    "Mictlan", "Olympus", "Styx", "Phlegethon", "Cocytus", "Acheron", "Lethe", "Elysium", "Tartarus", "Tir na nOg", "Mag Mell",
    "Emain Ablach", "Hy-Brasil", "Falias", "Gorias", "Findias", "Murias", "Hara Berezaiti", "Garo-Demanae", "Hamistagan", "Chinvat",
    "Irkalla",]
symbol_names = []

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
