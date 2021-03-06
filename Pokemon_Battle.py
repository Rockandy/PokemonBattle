# coding=utf-8
import random
import math
import os
import time

# All characters and music used in this game are Copyright (C) Game Freak 2016
# Alpha 0.1
"""
Damage Effect
Note: Pretty sure this is a more effective comment method, but whatever

How damageEffect works:
input the move type (Fight, Normal) and then the pokemon's type/types.
Function will return how effective the move is on the pokemon.
This function will need someone to make a damage function however
Also: No you cannot multiply these values by one.

Also: I'm going to go make a few changes to how damage works, I'll list them all here:
- Pokemon health will more accurately represent how actual health works, meaning that damage cannot be like 2,
it has to be like 100.
- All pokemon types will have to be put inside of a list

How to define a pokemon:
First entry: Name
2nd: Attack
3rd: Defense
4th: Speed
5th: Another list of moves
6th: Type list/1 String if only 1 type pokemon for everything
7th: Pokemon's Max Health

A = attacker's Level = 50
B = attacker's Attack or Special = Blah
C = attack Power = Must go and define those later on
D = defender's Defense or Special = Blah
X = Same-Type Attack Bonus [STAB] (1 or 1.5) = will go make a function
Y = Type modifiers (40, 20, 10, 5, 2.5, or 0) = Only if we're using damage/defense boosting moves
Z = a random number between 217 and 255

"""


def activateturn(opponentpokemon, playerpokemon):
    winner = 0
    playerhealth = playerpokemon[6]
    opponenthealth = opponentpokemon[6]

    while winner == 0:


        print("Enter 1 to use " + playerpokemon[4][0][0])
        print("Enter 2 to use " + playerpokemon[4][1][0])
        print("Enter 3 to use " + playerpokemon[4][2][0])
        print("Enter 4 to use " + playerpokemon[4][3][0])

        choice = playerpokemon[4][int(raw_input("")) - 1]
        opponentchoice = playerpokemon[4][random.randint(1, 4)]

        yourdamage = pokemonDamage(playerpokemon[1], choice[1], opponentpokemon[2], playerpokemon[6], choice[1])
        opponentdamage = pokemonDamage(
            (opponentpokemon[1], opponentchoice[1], playerpokemon[2], opponentpokemon[6], opponentchoice[1]))
        yourrecoil = recoil(playerpokemon[1], choice[1], opponentpokemon[2], playerpokemon[6], choice[1])
        opponentrecoil = recoil(opponentpokemon[1], opponentchoice[1], playerpokemon[2], opponentpokemon[6], opponentchoice[1])

        if playerpokemon[3] > opponentpokemon[3]:
            opponenthealth -= yourdamage
            print "You used " + choice[1] + "!"
            print ("Opponent took " + str(yourdamage) + "damage!")
            if opponenthealth <= 0 and winner == 0:
                winner = 1

            else:
                playerhealth -= yourrecoil
                if yourrecoil > 0: print("You took " + str(yourrecoil) + "in recoil damage.")
                if playerhealth <= 0 and winner == 0:
                    winner = -1
                else:
                    yourhealth -= opponentdamage
                    print "Opponent used" + opponentchoice[1]
                    print "You took " + str(opponentdamage) + "damage."
                    playerhealth -= opponentdamage
                    if playerhealth <= 0:
                        winner = -1
                    else:
                        opponenthealth -= opponentrecoil
                        if opponentrecoil > 0: print("Opponent took " + str(opponentrecoil) + "in recoil damage.")
                        if opponenthealth <= 0:
                            winner = 1

        else:
            yourthealth -= opponentdamage
            print ("You took " + str(yourdamage) + "damage!")
            if yourhealth <= 0 and winner == 0:
                winner = -1

            else:
                opponenthealth -= opponentrecoil
                if opponentrecoil > 0: print("You took " + str(yourrecoil) + "in recoil damage.")
                if opponenthealth <= 0 and winner == 0:
                    winner = 1
                else:
                    opponenthealth -= yourdamage
                    print "You used" + move
                    print "Opponent took " + str(yourdamage) + "damage."
                    opponenthealth -= yourdamage
                    if opponenthealth <= 0:
                        winner = 1
                    else:
                        yourhealth -= yourrecoil
                        if yourrecoil > 0: print("You took " + str(yourrecoil) + "in recoil damage.")
                        if yourhealth <= 0:
                            winner = -1


def damageeffect(move_type, pokemon_types):
    thing = 1
    for x in pokemon_types:
        if pokemon_types[x] == 'Normal':
            thing *= Normaltype(move_type)

        elif pokemon_types[x] == 'Fight':
            thing *= Fighttype(move_type)

        elif pokemon_types[x] == 'Flying':
            thing *= Flyingtype(move_type)

        elif pokemon_types[x] == 'Rock':
            thing *= Rocktype(move_type)

        elif pokemon_types[x] == 'Ground':
            thing *= Groundtype(move_type)

        elif pokemon_types[x] == 'Poison':
            thing *= Poisontype(move_type)

        elif pokemon_types[x] == 'Grass':
            thing *= Grasstype(move_type)

        elif pokemon_types[x] == 'Bug':
            thing *= Bugtype(move_type)

        elif pokemon_types[x] == 'Psychic':
            thing *= Psychictype(move_type)

        elif pokemon_types[x] == 'Ghost':
            thing *= Ghosttype(move_type)

        elif pokemon_types[x] == 'Dark':
            thing *= Darktype(move_type)

        elif pokemon_types[x] == 'Fairy':
            thing *= Fairytype(move_type)

        return thing


def pokemonDamage(b, c, d, pokemon_types, move_type):
    x = STAB(pokemon_types, move_type)
    z = random.randint(217, 255)
    output = math.ceil(((((((9 * (100 / 5 + 2) * b * c) / d) / 50) + 2) * x) * z) / 255)
    return output


def recoil(b, c, d, y, pokemon_types, move_type, move_name):
    if move_name == "Double Edge" or move_name == "Volt Tackle" or move_name == "Brave Bird" or move_name == "Wood Hammer":
        x = STAB(pokemon_types, move_type)
        z = random.randint(217, 255)
        output = math.ceil((((((((((100 / 5 + 2) * b * c) / d) / 50) + 2) * x) * y / 10) * z) / 255) / 4)
        return output
    else:
        return 0


def STAB(pokemon_types, move_type):
    for x in pokemon_types:
        if pokemon_types[x] == move_type: return 1.5


def misschance(move_accuracy):
    if move_accuracy >= random.randint(1, 100):
        return False
    else:
        return True


# Defensive
def Normaltype(opponent_type):
    if opponent_type == 'Fight':
        return 2
    elif opponent_type == 'Ghost':
        return 0
    else:
        return 1


def Fighttype(opponent_type):
    if opponent_type == 'Flying':
        return 2
    elif opponent_type == 'Rock':
        return 0.5
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Psychic':
        return 2
    elif opponent_type == 'Dark':
        return 0.5
    elif opponent_type == 'Fairy':
        return 2
    else:
        return 1


def Flyingtype(opponent_type):
    if opponent_type == 'Fight':
        return 0.5
    elif opponent_type == 'Ground':
        return 0
    elif opponent_type == 'Rock':
        return 2
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Grass':
        return 0.5
    elif opponent_type == 'Electr':
        return 2
    elif opponent_type == 'Ice':
        return 2
    else:
        return 1


def Poisontype(opponent_type):
    if opponent_type == 'Fight':
        return 0.5
    elif opponent_type == 'Poison':
        return 0.5
    elif opponent_type == 'Ground':
        return 2
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Grass':
        return 0.5
    elif opponent_type == 'Psychic':
        return 2
    elif opponent_type == 'Fairy':
        return 0.5
    else:
        return 1


def Groundtype(opponent_type):
    if opponent_type == 'Poison':
        return 0.5
    elif opponent_type == 'Rock':
        return 0.5
    elif opponent_type == 'Water':
        return 2
    elif opponent_type == 'Grass':
        return 2
    elif opponent_type == 'Electr':
        return 0
    elif opponent_type == 'Ice':
        return 2
    else:
        return 1


def Rocktype(opponent_type):
    if opponent_type == 'Normal':
        return 0.5
    elif opponent_type == 'Fight':
        return 2
    elif opponent_type == 'Flying':
        return 0.5
    elif opponent_type == 'Poison':
        return 0.5
    elif opponent_type == 'Ground':
        return 2
    elif opponent_type == 'Steel':
        return 2
    elif opponent_type == 'Fire':
        return 0.5
    elif opponent_type == 'Water':
        return 2
    elif opponent_type == 'Grass':
        return 2
    else:
        return 1


def Bugtype(opponent_type):
    if opponent_type == 'Fight':
        return 0.5
    elif opponent_type == 'Flying':
        return 2
    elif opponent_type == 'Ground':
        return 0.5
    elif opponent_type == 'Rock':
        return 2
    elif opponent_type == 'Fire':
        return 2
    elif opponent_type == 'Grass':
        return 0.5
    else:
        return 1


def Ghosttype(opponent_type):
    if opponent_type == 'Normal':
        return 0
    elif opponent_type == 'Fight':
        return 0
    elif opponent_type == 'Poison':
        return 0.5
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Ghost':
        return 2
    elif opponent_type == 'Dark':
        return 2
    else:
        return 1


def Steeltype(opponent_type):
    if opponent_type == 'Normal':
        return 0.5
    elif opponent_type == 'Fight':
        return 2
    elif opponent_type == 'Flying':
        return 0.5
    elif opponent_type == 'Poison':
        return 0
    elif opponent_type == 'Ground':
        return 2
    elif opponent_type == 'Rock':
        return 0.5
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Steel':
        return 0.5
    elif opponent_type == 'Fire':
        return 2
    elif opponent_type == 'Grass':
        return 0.5
    elif opponent_type == 'Psychic':
        return 0.5
    elif opponent_type == 'Ice':
        return 0.5
    elif opponent_type == 'Dragon':
        return 0.5
    elif opponent_type == 'Fairy':
        return 0.5
    else:
        return 1


def Firetype(opponent_type):
    if opponent_type == 'Ground':
        return 2
    elif opponent_type == 'Rock':
        return 2
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Steel':
        return 0.5
    elif opponent_type == 'Fire':
        return 0.5
    elif opponent_type == 'Water':
        return 2
    elif opponent_type == 'Grass':
        return 0.5
    elif opponent_type == 'Ice':
        return 0.5
    elif opponent_type == 'Fairy':
        return 0.5
    else:
        return 1


def Watertype(opponent_type):
    if opponent_type == 'Steel':
        return 0.5
    elif opponent_type == 'Fire':
        return 0.5
    elif opponent_type == 'Water':
        return 0.5
    elif opponent_type == 'Grass':
        return 2
    elif opponent_type == 'Electr':
        return 2
    elif opponent_type == 'Ice':
        return 0.5
    else:
        return 1


def Grasstype(opponent_type):
    if opponent_type == 'Flying':
        return 2
    elif opponent_type == 'Poison':
        return 2
    elif opponent_type == 'Ground':
        return 0.5
    elif opponent_type == 'Bug':
        return 2
    elif opponent_type == 'Fire':
        return 2
    elif opponent_type == 'Water':
        return 0.5
    elif opponent_type == 'Grass':
        return 0.5
    elif opponent_type == 'Electr':
        return 0.5
    elif opponent_type == 'Ice':
        return 2
    else:
        return 1


def Electrtype(opponent_type):
    if opponent_type == 'Flying':
        return 0.5
    elif opponent_type == 'Ground':
        return 2
    elif opponent_type == 'Steel':
        return 0.5
    elif opponent_type == 'Electr':
        return 0.5
    else:
        return 1


def Psychictype(opponent_type):
    if opponent_type == 'Fight':
        return 0.5
    elif opponent_type == 'Bug':
        return 2
    elif opponent_type == 'Ghost':
        return 2
    elif opponent_type == 'Psychic':
        return 0.5
    elif opponent_type == 'Dark':
        return 2
    else:
        return 1


def Icetype(opponent_type):
    if opponent_type == 'Fight':
        return 2
    elif opponent_type == 'Rock':
        return 2
    elif opponent_type == 'Steel':
        return 2
    elif opponent_type == 'Fire':
        return 2
    elif opponent_type == 'Ice':
        return 0.5
    else:
        return 1


def Dragontype(opponent_type):
    if opponent_type == 'Fire':
        return 0.5
    elif opponent_type == 'Water':
        return 0.5
    elif opponent_type == 'Grass':
        return 0.5
    elif opponent_type == 'Electr':
        return 0.5
    elif opponent_type == 'Ice':
        return 2
    elif opponent_type == 'Dragon':
        return 2
    elif opponent_type == 'Fairy':
        return 2
    else:
        return 1


def Darktype(opponent_type):
    if opponent_type == 'Fight':
        return 2
    elif opponent_type == 'Ghost':
        return 2
    elif opponent_type == 'Steel':
        return 0.5
    elif opponent_type == 'Psychic':
        return 0
    elif opponent_type == 'Dark':
        return 0.5
    elif opponent_type == 'Fairy':
        return 2
    else:
        return 1


def Fairytype(opponent_type):
    if opponent_type == 'Fight':
        return 0.5
    elif opponent_type == 'Poison':
        return 2
    elif opponent_type == 'Bug':
        return 0.5
    elif opponent_type == 'Steel':
        return 2
    elif opponent_type == 'Dragon':
        return 0
    elif opponent_type == 'Dark':
        return 0.5
    else:
        return 1


"""
How to define a move:
First entry: Name of move
2nd: Move type
3rd: Move power
4th: Accuracy
"""
'''
4 Moves Per Set??
NO, WE DON'T NEED FOUR MOVES
WE ONLY NEED WHAT WE NEED
WE'RE DEFINING POKEMON WE CAN CHOOSE WHAT WE NEED
'''

# Normal
Body_Slam = ['Body Slam', 'Normal', 85, 100]
Splash = ['Splash', 'Normal', 0, 100]  # Best move
Tri_Attack = ['Tri Attack', 'Normal', 80, 100]
Slash = ['Slash', 'Normal', 70, 100]
Double_Edge = ['Double Edge', 'Normal', 120, 90]  # Recoil
Hyper_Voice = ['Hyper Voice', 'Normal', 90, 100]
# Fighting
Brick_Break = ['Brick Break', 'Fight', 75, 100]
Close_Combat = ['Close Combat', 'Fight', 120, 70]
Sky_Uppercut = ['Sky Uppercut', 'Fight', 85, 90]
Cross_Chop = ['Cross Chop', 'Fight', 100, 80]
Focus_Blast = ['Focus Blast', 'Fight', 120, 65]
# Flying
Air_Slash = ['Air Slash', 'Flying', 75, 95]
Fly = ['Fly', 'Flying', 90, 95]
Bounce = ['Bounce', 'Flying', 85, 90]
Hurricane = ['Hurricane', 'Flying', 110, 70]
Brave_Bird = ['Brave Bird', 'Flying', 120, 100]
# Poison
Sludge_Bomb = ['Sludge Bomb', 'Poison', 90, 100]
Cross_Poison = ['Cross Poison', 'Poison', 70, 100]
Poison_Jab = ['Poison Jab', 'Poison', 80, 100]
Gunk_Shot = ['Gunk Shot', 'Poison', 120, 80]
# Ground
Earth_Power = ['Earth Power', 'Ground', 90, 100]
Earthquake = ['Earthquake', 'Ground', 90, 100]
Fissure = ['Fissure', 'Ground', 200, 30]
# Rock
Stone_Edge = ['Stone Edge', 'Rock', 100, 80]
Power_Gem = ['Power Gem', 'Rock', 80, 100]
Ancient_Power = ['Ancient Power', 'Rock', 80, 100]
Rock_Wrecker = ['Rock Wrecker', 'Rock', 150, 50]
# Bug
Megahorn = ['Megahorn', 'Bug', 120, 85]
X_Scissor = ['X-Scissor', 'Bug', 80, 100]
Signal_Beam = ['Signal Beam', 'Bug', 75, 100]
Bug_Bite = ['Bug Bite', 'Bug', 60, 100]
# Ghost
Shadow_Ball = ['Shadow Ball', 'Ghost', 80, 100]
Shadow_Claw = ['Shadow Claw', 'Ghost', 70, 100]
Ominous_Wind = ['Ominous Wind', 'Ghost', 60, 100]
# Steel
Flash_Cannon = ['Flash Cannon', 'Steel', 80, 100]
Meteor_Mash = ['Meteor Mash', 'Steel', 90, 90]
Iron_Head = ['Iron Head', 'Steel', 80, 100]
Iron_Tail = ['Iron Tail', 'Steel', 100, 75]
Steel_Wing = ['Steel Wing', 'Steel', 70, 95]
# Fire
Flamethrower = ['Flamethrower', 'Fire', 90, 100]
Blaze_Kick = ['Blaze Kick', 'Fire', 85, 90]
Heat_Wave = ['Heat Wave', 'Fire', 95, 90]
Fire_Blast = ['Fire Blast', 'Fire', 110, 80]
# Water
Waterfall = ['Waterfall', 'Water', 80, 100]
Aqua_Tail = ['Aqua Tail', 'Water', 90, 90]
Surf = ['Surf', 'Water', 90, 100]
Hydro_Pump = ['Hydro Pump', 'Water', 110, 80]
Magikarps_Revenge = ["Magikarp's Revenge", 'Water', 50000000, 200]
# Grass
Mystic_Leaf = ['Razor Leaf', 'Grass', 60, 200]
Energy_Ball = ['Energy Ball', 'Grass', 90, 100]
Seed_Bomb = ['Seed Bomb', 'Grass', 80, 100]
Wood_Hammer = ['Wood Hammer', 'Grass', 100, 80]
Power_Whip = ['Power Whip', 'Grass', 120, 85]
# Electr
Zap_Cannon = ['Zap Cannon', 'Electr', 120, 60]
Thunder = ['Thunder', 'Electr', 110, 70]
Thunderbolt = ['Thunderbolt', 'Electr', 90, 100]
Volt_Tackle = ['Volt Tackle', 'Electr', 120, 100]  # Recoil
# Psychic
Psychic = ['Psychic', 'Psychic', 90, 100]
Psycho_Cut = ['Psycho Cut', 'Psychic', 70, 100]
Extrasensory = ['Extrasensory', 'Psychic', 80, 100]
Zen_Headbutt = ['Zen Headbutt', 'Psychic', 85, 90]
# Ice
Ice_Beam = ['Ice Beam', 'Ice', 95, 100]
Ice_Punch = ['Ice Punch', 'Ice', 75, 100]
Blizzard = ['Blizzard', 'Ice', 110, 70]
Aurora_Beam = ['Aurora Beam', 'Ice', 65, 100]
# Dragon
Dragon_Rush = ['Dragon Rush', 'Dragon', 100, 75]
Dragon_Pulse = ['Dragon Pulse', 'Dragon', 85, 100]
Dragon_Claw = ['Dragon Claw', 'Dragon', 80, 100]
Draco_Meteor = ['Draco Meteor', 'Dragon', 130, 60]
# Dark
Dark_Pulse = ['Dark Pulse', 'Dark', 80, 100]
Crunch = ['Crunch', 'Dark', 80, 100]
Night_Slash = ['Night Slash', 'Dark', 70, 100]
Foul_Play = ['Foul Play', 'Dark', 95, 95]
Night_Daze = ['Night Daze', 'Dark', 95, 95]
# Fairy
Dazzling_Gleam = ['Dazzling Gleam', 'Fairy', 80, 100]
Play_Rough = ['Play Rough', 'Fairy', 90, 90]
Moonblast = ['Moonblast', 'Fairy', 95, 95]

"""
How to define a pokemon:
First entry: Name
2nd: Attack
3rd: Defense
4th: Speed
5th: Another list of moves
6th: Type list/1 String if only 1 type pokemon for everything
7th: Pokemon's Max Health
"""

# Mew = ["Mew", 100, 100, 100,[Ice_Beam, Psychic, Discharge, Air_Slash], 'Psychic', 210]
Raichu = ["Raichu", 95, 80, 110, [Thunderbolt, Iron_Tail, Thunder, Double_Edge], 'Electr', 630]
Zoroark = ["Zoroark", 120, 60, 105, [Night_Daze, Foul_Play, Flamethrower, Hyper_Voice], 'Dark', 580]
Snorlax = ["Snorlax", 110, 110, 30, [Body_Slam, Crunch, Earthquake, Surf], 'Normal', 700]
Wailord = ["Wailord", 95, 60, 60, [Hydro_Pump, Bounce, Blizzard, Earthquake], 'Water', 950]
Dusknoir = ["Dusknoir", 110, 135, 50, [Shadow_Ball, Psychic, Focus_Blast, Dark_Pulse], 'Ghost', 620]
Staraptor = ["Staraptor", 120, 70, 100, [Fly, Close_Combat, Brave_Bird, Steel_Wing], 'Flying', 600]
Tangrowth = ["Tangrowth", 110, 125, 50, [Power_Whip, Ancient_Power, Energy_Ball, Sludge_Bomb], 'Grass', 660]
Beartic = ["Beartic", 115, 85, 60, [Surf, Blizzard, Ice_Beam, Focus_Blast], 'Ice', 610]
Magmortar = ["Magmortar", 125, 95, 83, [Flamethrower, Focus_Blast, Thunderbolt, Fire_Blast], 590]
Alakazam = ["Alakazam", 135, 80, 120, [Psychic, Psycho_Cut, Shadow_Ball, Focus_Blast], 'Psychic', 570]
Muk = ["Muk", 105, 100, 50, [Sludge_Bomb, Gunk_Shot, Shadow_Ball, Fire_Blast], 'Poison', 620]
Haxorus = ["Haxorus", 145, 90, 97, [Dragon_Pulse, Draco_Meteor, Shadow_Claw, Earthquake], 'Dragon', 590]
Machamp = ["Machamp", 135, 85, 65, [Cross_Chop, Focus_Blast, Stone_Edge, Poison_Jab], 'Fight', 620]
Klinklang = ["Klinklag", 100, 115, 90, [Zap_Cannon, Flash_Cannon, Signal_Beam, Thunderbolt], 'Steel', 570]
Florges = ["Florges", 110, 150, 75, [Moonblast, Energy_Ball, Dazzling_Gleam, Psychic], 'Fairy', 590]
Donphan = ["Donphan", 120, 125, 50, [Earthquake, Stone_Edge, Poison_Jab, Seed_Bomb], 'Ground', 600]
Gigalith = ["Gigalith", 130, 125, 25, [Earthquake, Stone_Edge, Iron_Head, Power_Gem], 'Rock', 580]
Pinsir = ["Pinsir", 125, 100, 85, [X_Scissor, Stone_Edge, Brick_Break, Earthquake], 'Bug', 600]
Magikarp = ["Magikarpet", 50, 55, 80, [Splash, Splash, Splash, Magikarps_Revenge], 'Water', 530]  # Magikarp for the win
Feebas = ["Feebas", 15, 55, 80, [Splash, Splash, Splash, Splash], 'Water', 1000]

'''
Should I put Ai/ what the computer says and calculates what the health of the pokemon goes down/ something
Do you understand?: AI is going to be really stupid, and the calculations can just be done by using 2 variables
That's what I mean, like it chooses one randomly, or actually spam a good move that is effective
random, otherwise it would be too repetitive.
BUT WAIT, OUR GAME IS ALREADY REPETITIVE
D:
'''

# Intro Flavor Text
print("\033[32;0;0mHello There! Welcome to the world of Pokemon! \n")
time.sleep(2)
print(
"\033[32;0;0mMy name is Oak! People call me the Pokemon Prof! This world is inhabited by creatures called Pokemon!")
print(
"\033[32;0;0mFor some people, Pokemon are pets. Other use them for fights. Myself... I study Pokemon as a profession.\n")
time.sleep(5)
name_answer = ''
name = raw_input("\033[32;0;0mFirst, what is your name? ")
while name_answer.lower() != 'yes':
    print "Right! So your name is " + name + "."  # lol we can replace name with something stupid lol
    name_answer = raw_input("Yes or No: ")
    if name_answer.lower() != "yes":
        name = raw_input("\033[32;0;0mOkay, then what is your name? \n")
print ""
print "This is my grandson. He's been your rival since you were a baby."
time.sleep(1)
comp_name = raw_input("...Erm, what is his name again? ")
print "That's right! I remember now! His name is " + comp_name + "!"
print ""
time.sleep(1)
print name + ", your very own Pokemon legend is about to unfold!"
" A world of dreams and adventures with Pokemon awaits!"
print 'But first, you need to pick a Pokemon!'
print ""
time.sleep(2)
print 'Enter 1 for an Snorlax, 2 for a Wailord, 3 for a Dusknoir, 4 for a Staraptor, 5 for a Tangrowth, 6 for a Beartic'
print '7 for a Magmortar, 8 for a Alakazam, 9 for a Muk, 10 for a Raichu, 11 for a Haxorus, 12 for a Machamp,'
print '13 for a Kinklang, 14 for a Florges, 15 for a Zoarark, 16 for a Donphan, 17 for a Gigalith, '
print 'and 18 for a Pinsir.'
print ""
answer = int(raw_input("Choose a pokemon: "))

if answer == 1:
    print "You have chosen a Snorlax!"
    playerpokemon = Snorlax
elif answer == 2:
    print "You have chosen a Wailord!"
    playerpokemon = Wailord
elif answer == 3:
    print "You have chosen a Dusknoir!"
    playerpokemon = Dusknoir
elif answer == 4:
    print "You have chosen a Staraptor!"
    playerpokemon = Staraptor
elif answer == 5:
    print "You have chosen a Tangrowth!"
    playerpokemon = Tangrowth
elif answer == 6:
    print "You have chosen a Beartic!"
    playerpokemon = Beartic
elif answer == 7:
    print "You have chosen a Magmortar!"
    playerpokemon = Magmortar
elif answer == 8:
    print "You have chosen a Alakazam!"
    playerpokemon = Alakazam
elif answer == 9:
    print "You have chosen a Muk!"
    playerpokemon = Muk
elif answer == 10:
    print "You have chosen a Raichu!"
    playerpokemon = Raichu
elif answer == 11:
    print "You have chosen a Haxorus!"
    playerpokemon = Haxorus
elif answer == 12:
    print "You have chosen a Machamp!"
    playerpokemon = Machamp
elif answer == 13:
    print "You have chosen a Klingklang!"
    playerpokemon = Klinklang
elif answer == 14:
    print "You have chosen a Florges!"
    playerpokemon = Florges
elif answer == 15:
    print "You have chosen a Zoarark!"
    playerpokemon = Zoroark
elif answer == 16:
    print "You have chosen a Donphan!"
    playerpokemon = Donphan
elif answer == 17:
    print "You have chosen a Gigalith!"
    playerpokemon = Gigalith
elif answer == 18:
    print "You have chosen a Pinsir!"
    playerpokemon = Pinsir
elif answer == 0:
    print "You have chosen the top percentage Magikarp of all Magikarps!"
    playerpokemon = Magikarp
else:
    print "I am sorry. That was not on the list. We will give you a worthless but rare Feebas instead."
    playerpokemon = Feebas