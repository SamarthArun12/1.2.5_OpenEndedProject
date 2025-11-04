import turtle as trtl
import random
from skill_class import Skill

player_skill1 = Skill(4, 4, 3)
enemy_skill1 = Skill(3, 3, 4)

def clashing(p_skill, e_skill):
    p_coins = p_skill.initial_coins()
    e_coins = e_skill.initial_coins()
    clash = True
    while clash:
        p_num = p_skill.calculate(p_coins)
        e_num = e_skill.calculate(e_coins)
        if p_num > e_num:
            e_coins -= 1
        elif e_num > p_num:
            p_coins -= 1
        #nobody loses coins if roll same number
        if e_coins == 0:
            loser = "enemy" #placeholder, change later to enemy object
            damage_num = p_skill.calculate(p_coins)
            clash = False
        elif p_coins == 0:
            loser = "player" #placeholder, change later to player object
            damage_num = e_skill.calculate(e_coins)
            clash = False
    return loser, damage_num

lost, damage_to_take = clashing(player_skill1, enemy_skill1)

print(lost + " takes " + str(damage_to_take) + " damage!")
