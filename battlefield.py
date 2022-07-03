from robot import Robot
from dinosaur import Dinosaur
import random

class Battlefield:
    winner = ''
    def __init__(self):
        self.robot = Robot('yx23')
        self.dinosaur = Dinosaur('baryxonix', 22)
    def run_game(self):
        self.display_welcome()
        while self.dinosaur.dino_health > 0 or self.robot.robot_health > 0:
            self.battle_phase()
            # order = random.choice([1,2])
            # if order == 1:
            #     self.robot.attack(self.dinosaur)
            if self.dinosaur.dino_health <= 0 or self.robot.robot_health <= 0:
                global winner
                print("GameOver")
                if self.dinosaur.dino_health <= 0:
                    winner = self.robot.robot_name
                    self.display_winner()
                    break
                else:
                    winner = self.dinosaur.dino_name
                    self.display_winner()
                    break

    def display_welcome(self):
        print("welcome to the fight, the game is between the robot and the dinosaur!\nlet's run it.")
        # welcomed = True

    def battle_phase(self):
        players = (self.robot.robot_name, self.dinosaur.dino_name)
        selected = random.choice(players)
        if selected == self.robot.robot_name:
            yea = True
            if yea == True:
                not_selected = self.dinosaur.dino_name
                print(f"the {selected} has attacked the {not_selected} with his {self.robot.robot_active_weapon.weapon_name} and damaged {self.robot.robot_active_weapon.weapon_attack_power} to the him")
                self.dinosaur.dino_health -= self.robot.robot_active_weapon.weapon_attack_power
                print(f"and dinosaur's health is at {self.dinosaur.dino_health} now!")
        else:
            yea = False
            if yea == False:
                not_selected = self.robot.robot_name
                print(f"the {selected} has attacked the {not_selected} and damaged {self.dinosaur.dino_attack_power} to the him")
                self.robot.robot_health -= self.dinosaur.dino_attack_power
                print(f"and robot's health is at {self.robot.robot_health} now!")

    def display_winner(self):
        if winner == self.robot.robot_name:
            print("Robot is the winner of this game!\ni'm sure Dinosaur will be back stronger.")
        else:
            print("Dinosaur is the winner of this game!\ni'm sure Robot will be back stronger.")
