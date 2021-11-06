# pvp_battle.py
# written by David McCabe

'''
This program holds the logic for the fighting backend between two Fighters
'''

from SCP.Fighter.Fighter import Fighter
from SCP.Move.MovesList import MoveList
# from GUI.Battle.screen import Battle_Screen
import random

# Reads user fighter data in user_info.txt
def read_info():
    user_info = dict()
    with open("user_info.txt", "r") as g:
        for i in g.readlines():
            split = i.index(":")
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
def make_fighter(name, level, attack, defense, health, moves):
    return Fighter(name, level, attack, defense, health, moves)

# Returns size 2 array: (successful attack), (target fainted)
def Attack(Attacker, Target, Move):
    target_damage = Move.baseDmg * (Attacker.level / Target.level) * (Attacker.attack/Target.defense)
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
def Battle(user, fighter2):
    move_list = MoveList()
    f2_poss_moves = fighter2.getMoves()
    f2_total_moves = len(f2_poss_moves)
    while(not user.IsDead() and not fighter2.IsDead()):
        sc = Battle_Screen()
        next_move = move_list[sc.move_select()]
        # Chooses a random move from the possible moves of computer
        f2_move = move_list[f2_poss_moves[random.randint(0, f2_total_moves - 1)]]
        if random.random() > .5:
            outcome = Attack(user, fighter2, next_move)
            # user move missed
            if not outcome[1]:
                pass
            elif outcome[2]: break
            outcome  = Attack(fighter2, user, f2_move)
            # opponent move missed
            if not outcome[1]:
                pass
        else:
            outcome  = Attack(fighter2, user, f2_move)
            # opponent move missed
            if not outcome[1]:
                pass
            elif outcome[2]: break
            outcome = Attack(user, fighter2, next_move)
            # user move missed
            if not outcome[1]:
                pass

    # Stat updates
    user.addExperience(fighter2.level)
    user.fullHeal()

    # Storyline
    if not user.IsDead(): return True
    return False


