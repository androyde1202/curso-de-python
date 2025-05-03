equipamento=str(input("qual equipamento você dejesa melhorar coloque com todas asprimeiras çetras maiusculas e em ingles:"))
raridade=str("")
if equipamento == "Giant Gauntlet" or "Spiky Ball" or "Snake Bracelet" or "Frozen Arrow" or "Magic Mirror" or "Action Figure" or "Fireball" or "Lavaloon Puppet" or "Rocket Spear" or "Electro Boots":
    raridade=str("epica")
elif equipamento == "Barbarian Puppet" or "Rage Vial" or "Earthquake Boots" or "Vampstache" or "Archer Puppet" or "Invisibility Vial" or  "Giant Arrow" or "Healer Puppet" or "Dark Orb" or "Henchmen Puppet" or "Metal Pants" or "Noble Iron" or "Eternal Tome" or "Life Gem" or "Rage Gem" or "Healing Tome" or "Royal Gem" or "Seeking Shield" or "Hog Rider Puppet" or "Haste Vial":
    raridade=str("comum")
else :
    print("digite um equipamento valido")

