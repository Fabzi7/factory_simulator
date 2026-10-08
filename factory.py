import buildings.json

class Factory:
    def __init__(self, player, Cash=100):
        self.player = player
        self.resources = {}
        self.staff = {}
        self.research_points = 0
        self.buildings = {}
        self.max_staff = 5
        print(f"{player.name}'s factory initialised.")

    def add_building(self, building):
        self.buildings[building] += 1
        self.player.cash -= self.building["Cost"]
        #start off

    def hire_staff(self, staff):
        self.cash -= staff["Hire Cost"]
        #self.pay_staff(staff["Wage"])
        self.staff += staff

    

    