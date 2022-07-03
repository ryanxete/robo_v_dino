class Dinosaur:
    def __init__(self, name, attack_power):
        self.dino_name = name
        self.dino_attack_power = attack_power
        self.dino_health = 100

    def attack(self, robot):
        print(f"the {self.dino_name} has attacked the {robot.robot_name} and damaged {self.dino_attack_power} to the robot")
        robot.robot_health -= self.dino_attack_power
        print(f"and robot's health is at {robot.robot_health} now!")