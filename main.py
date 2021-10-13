from Dinosaur import Dinasaur
from Weapons import Weapon
from Robot import Robot


sword=Weapon()
print(sword.name)
print(sword.attack_power, "is the attack power.")


robot1=Robot()
robot2=Robot()
robot3=Robot()

print("Your Robot fleet consist of ", robot1.name,",",robot2.name,",",robot3.name,".")

dino1=Dinasaur()
dino2=Dinasaur()
dino3=Dinasaur()

print("Your Dino herd consist of ", dino1.name,",",dino2.name,",",dino3.name,".")







