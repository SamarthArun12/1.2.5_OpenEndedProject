import turtle as trtl
import random
from skill_class import Skill

player_skill1 = Skill(4, 4, 3)
enemy_skill1 = Skill(3, 3, 4)
print(player_skill1.calculate())
print(enemy_skill1.calculate())
