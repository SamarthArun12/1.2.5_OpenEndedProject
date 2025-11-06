import turtle as trtl
import random
import time
from skill_class import Skill

player_skill1 = Skill(4, 4, 3, "Player Skill 1")
enemy_skill1 = Skill(3, 3, 4, "Enemy Skill 1")

print(player_skill1.calculate(3))
print(enemy_skill1.calculate(4))
