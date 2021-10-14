from Robot import Robot


class Fleet:
    def __init__(self):
        self.robots=[]
         
    def create_fleet(self):
        robot1=Robot("Tron",500)
        self.robots.append(robot1)
        robot2=Robot("Optimus",620)
        self.robots.append(robot2)
        robot3=Robot("Tekkum",450)
        self.robots.append(robot3)
fleet=Fleet()
fleet.create_fleet()
print(fleet.robots)