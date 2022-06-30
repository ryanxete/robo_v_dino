from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 0
        self.robot_active_weapon = Weapon('chainsword', 18)

    def attack(self, dinosaur):
        pass