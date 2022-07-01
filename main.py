# (10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.
# (10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.
# (10 points): As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.
# Bonus Points:
# (5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack.
# (5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

from battlefield import Battlefield

battlefield_1 = Battlefield()
battlefield_1.run_game()