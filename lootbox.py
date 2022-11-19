
class Loot:

    def __init__(self):
        self.item = ["Frost Potion:\n\n+2 AC \n+4 Frost resistance",
                     "Small Health Potion:\n\n+2d4 HP",
                     "Large Health Potion:\n\n +4d6 HP",
                     "Health Potion:\n\n +2d6 HP",
                     "Swift Pottion: \n\n +10 Movement speed\n\n Duration: 1 Hour",
                     "Liquid Armor: \n\n +5 AC\n\n Duration: 1 Hour",
                     "Advantage Potion: \n\n +1 Advantage",
                     "Antidote Potion: \n\n Cures all ailments",
                     "Breathing Potion:\n\nUnderWater Breathing\n\nDuration: 1 Hour",
                     "Fey Honey: \n\n +7 Charisma\n\n Duration: 2 Hours",
                     "Berserker's Toxin:\n\n +6 Strength\n\n Duration: 30 min",
                     "Monkey Wine:\n\n +5 Dexterity\n\n Duration: 1 Hour",
                     "Potion of Wisdom:\n\n +5 Wisdom\n\n Duration: 1 Hour",
                     "Algernon's Ale: \n\n +7 Intelligence\n\n Duration 2 Hours",
                     "Potion of Toughness:\n\n+5 Constitution\n\n Duration 1 Hour",
                     ]
        self.armor = ["Brace","Chest Armor", "Shield", "Belt", "Boots", "Gloves", "Helmet"]
        self.weapon = ["LightHammer", "Warhammer","MorningStar","Club","Maul",
                       "Sword", "Whip","HandAxe", "Long Sword", "Halberd", "Greatsword", "Scimitar",
                       "Dagger", "Javelin", "Shortbow", "Rapier", "Lance", "Dart", "Trident", "War Pick",
                       "Spear", "Crossbow", "Longbow"
                       ]
        self.stats = ["Strength", "Constitution","Dexterity","Charisma","Intelligence","Wisdom"]
        self.buff = ["+1d6 Poison", "+1d6 Frost", "+1d6 Flame", "+1d6 Acid", "1d6 Necro ", "None" ]
        self.dice = ["D4", "D6", "D8", "D10", "D12", "D20"]
