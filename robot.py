from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 100
        self.robot_active_weapon = Weapon("axe", 22)

    def attack(self, dinosaur):
        pass

    # def choose_weapons(self):
    #     # welcomed = False
    #     # while welcomed == True:
    #     chosen_weapon = input("choose robot's weapon from the options below!\n1.knife: damage = 19     2.chainsword: damage = 24      3.axe: 22\nenter your desired number!")
    #     if chosen_weapon == "1":
    #         chosen = Weapon('knife', 19)
    #     elif chosen_weapon == "2":
    #         chosen = Weapon('chainsword', 24)
    #     elif chosen_weapon == "3":
    #         chosen = Weapon('axe', 22)
    #     return chosen