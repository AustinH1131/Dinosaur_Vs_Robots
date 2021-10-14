from Dinosaur import Dinasaur
from Fleet import Fleet
from Weapons import Weapon
from Robot import Robot
from Herd import Herd


sword=Weapon()
print(sword.name)
print(sword.attack_power, "is the attack power.")

fleet=Fleet()
fleet.create_fleet()
print(fleet.robots)

herd=Herd()
herd.create_herd()
print(herd.dinasaurs)







