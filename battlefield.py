from robot import Robot
from dinosaur import Dinosaur
import random

class Battlefield:
    winner = ''
    def __init__(self):
        self.robot = Robot('yx23')
        self.dinosaur = Dinosaur('baryxonix', 23)

    def run_game(self):
        self.display_welcome()
        while self.dinosaur.dino_health > 0 or self.robot.robot_health > 0:
            self.battle_phase()
        
    def display_welcome(self):
        print("welcome to the fight, the game is between the robot and the dinosaur!\nlet's run it.")

    def battle_phase(self):
        players = (self.robot.robot_name, self.dinosaur.dino_name)
        selected = random.choice(players)
        if selected == self.robot.robot_name:
            self.robot.attack(self.dinosaur)
        else:
            self.dinosaur.attack(self.robot)
        if self.dinosaur.dino_health <= 0 or self.robot.robot_health <= 0:
            global winner
            print("GameOver")
            if  self.dinosaur.dino_health <= 0:
                winner = self.robot.robot_name
                self.display_winner()
            else:
                winner = self.dinosaur.dino_name
                self.display_winner()

    def display_winner(self):
        if winner == self.robot.robot_name:
            print("Robot is the winner of this game!\ni'm sure Dinosaur will be back stronger.")
        else:
            print("Dinosaur is the winner of this game!\ni'm sure the Robot will be back stronger.")
