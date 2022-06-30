from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("yx23")
        self.dinosaur = Dinosaur("baryxonix", 26)
        print(self.robot.robot_name)
    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass