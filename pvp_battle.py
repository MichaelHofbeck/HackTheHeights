# pvp_battle.py
# written by David McCabe

'''
This program holds the logic for the fighting backend between two Fighters
'''

from SCP.Fighter.Fighter import Fighter
from SCP.Move.MovesList import MoveList
# from GUI.Battle.screen import Battle_Screen
import random
from time import sleep

# Reads user fighter data in user_info.txt
def read_info():
    user_info = dict()
    with open("user_info.txt", "r") as g:
        for i in g.readlines():
            split = i.index(":")
            if(i[:split] != "Moves" and i[:split] != "Name"):
                user_info[i[:split]] = int(i[split + 2:])
            else:
                user_info[i[:split]] = i[split + 2:].strip()
        user_info["Moves"] = [x.strip() for x in user_info["Moves"].split(",")]
    return user_info

def write_user(user_fighter):
    with open("user_info.txt", "w") as f:
        f.write("Name: " + user_fighter.name + "\n")
        f.write("Attack: " + user_fighter.attack + "\n")
        f.write("Defense: " + user_fighter.defense + "\n")
        f.write("Experience: " + user_fighter.experience + "\n")
        f.write("Health: " + user_fighter.health + "\n")
        f.write("Level: " + user_fighter.level + "\n")
        f.write("MaxHealth: " + user_fighter.maxhealth + "\n")
        move_str = ""
        for name in user_fighter.moves: move_str += name + ", "
        move_str = move_str[:-2]
        f.write("Moves: " + move_str + "\n")

# Returns instance of Fighter
def make_fighter():
    d = read_info()
    name, level, attack, defense, health, moves, maxhealth, experience = d["Name"], d["Level"], d["Attack"], d["Defense"], d["Health"], d["Moves"], d["Experience"], d["MaxHealth"] 
    return Fighter(name, level, attack, defense, health, moves, maxhealth, experience)

# returns list of user moves
def get_user_moves():
    return read_info()["Moves"]

# Returns size 2 array: (successful attack), (target fainted)
def Attack(Attacker, Target, Move):
    target_damage = round(Move.baseDmg * (1.1**(Attacker.level / Target.level)) * (1.1**(Attacker.attack/Target.defense)))
    success_chance = Move.successRt
    if random.random() < success_chance:
        Target.Damage(target_damage)
        if Target.IsDead():
            return True, True
        else:
            return True, False
    else:
        return False, False

# Runs Battle functions
# Returns True if user wins, else False
def Battle(user, fighter2, move = -1):
    move_list = MoveList()
    f2_poss_moves = fighter2.getMoves()
    f2_total_moves = len(f2_poss_moves)
    print(get_user_moves())
    while(not user.IsDead() and not fighter2.IsDead()):
        print(user.name + ": " + str(user.health))
        print(fighter2.name + ": " + str(fighter2.health))
        next_move = move_list[get_user_moves()[move]]
        # Chooses a random move from the possible moves of computer
        f2_move = move_list[f2_poss_moves[random.randint(0, f2_total_moves - 1)]]
        print(get_user_moves()[move], next_move.successRt, next_move.baseDmg)
        if random.random() > .5:
            outcome = Attack(user, fighter2, next_move)
            # user move missed
            if not outcome[0]:
                pass
            elif outcome[1]: break
            outcome  = Attack(fighter2, user, f2_move)
            # opponent move missed
            if not outcome[0]:
                pass
        else:
            outcome  = Attack(fighter2, user, f2_move)
            # opponent move missed
            if not outcome[0]:
                pass
            elif outcome[1]: break
            outcome = Attack(user, fighter2, next_move)
            # user move missed
            if not outcome[0]:
                pass

    # Stat updates
    user.addExperience(4*fighter2.level)

    # Storyline
    if not user.IsDead(): 
        print("User Wins!")
        return True
    print("User Died!")
    return False

# user = make_fighter()
# opponent1 = Fighter(name="Naomi", level=1, attack=5, defense=15, health=20, moves=["ramble and shamble"], experience=1, maxhealth=20)
# print(Battle(user, opponent1))
# user.fullHeal()
# opponent2 = Fighter(name="Carl", level=1, attack=15, defense=5, health=18, moves=["ramble and shamble"], experience=1, maxhealth=18)
# print(Battle(user, opponent2))