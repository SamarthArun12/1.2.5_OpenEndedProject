import turtle as trtl
import random
import time
from skill_class import Skill

player_skill1 = Skill(4, 4, 3, "Player Skill 1")
enemy_skill1 = Skill(3, 3, 4, "Enemy Skill 1")

def clashing(p_skill, e_skill):
    p_coins = p_skill.initial_coins()
    e_coins = e_skill.initial_coins()
    clash = True
    while clash:
        p_num = p_skill.calculate(p_coins)
        e_num = e_skill.calculate(e_coins)
        print("Player rolls a " + str(p_num))
        time.sleep(0.5)
        print("Enemy rolls a " + str(e_num))
        time.sleep(0.5)
        if p_num > e_num:
            e_coins -= 1
            time.sleep(0.5)
            print("Enemy loses 1 coin and has " + str(e_coins) + " remaining!")
        elif e_num > p_num:
            p_coins -= 1
            time.sleep(0.5)
            print("Player loses 1 coin and has " + str(p_coins) + " remaining!")
        time.sleep(1)
        print(" ")
        #nobody loses coins if roll same number
        if e_coins == 0:
            loser = "enemy" #placeholder, change later to enemy object
            damage_num = p_skill.calculate(p_coins)
            skill_name = p_skill.get_name()
            print("Player attacks with " + str(p_coins) + " coins!")
            clash = False
        elif p_coins == 0:
            loser = "player" #placeholder, change later to player object
            damage_num = e_skill.calculate(e_coins)
            skill_name = e_skill.get_name()
            print("Enemy attacks with " + str(e_coins) + " coins!")
            clash = False
    return loser, damage_num, skill_name

lost, damage_to_take, skills_name = clashing(player_skill1, enemy_skill1)

print(lost + " takes " + str(damage_to_take) + " damage to " + skills_name + "!")
