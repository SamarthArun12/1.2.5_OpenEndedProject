import random

class Skill:

    def __init__(self, base_power, coin_power, coin_num, name):
        self.b_power = base_power
        self.c_power = coin_power
        self.c_num = coin_num
        self.name = name
    
    def __read__(self):
        return self.b_power, self.c_power, self.c_num, self.name
    
    def get_name(self):
        return self.name

    def initial_coins(self):
        return self.c_num

    def calculate(self, coins):
        final_power = self.b_power
        for i in range(0, coins):
            headsortails = random.randint(1,2)
            if headsortails == 1:
                final_power += self.c_power
        
        return final_power
