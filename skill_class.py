import random

class Skill:

    def __init__(self, base_power, coin_power, coin_num):
        self.b_power = base_power
        self.c_power = coin_power
        self.c_num = coin_num
    
    def __read__(self):
        return self.b_power, self.c_power, self.c_num

    def calculate(self):
        final_power = self.b_power
        for i in range(0, self.c_num):
            headsortails = random.randint(1,2)
            if headsortails == 1:
                final_power += self.c_power
        
        return final_power