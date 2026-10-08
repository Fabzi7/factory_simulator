import json

class Factory:
    def __init__(self, player, cash=1000, file_name = "buildings.json"):
        
        #attributes
        self.player = player
        self.cash = cash
        self.resources = {}
        self.staff = {}
        self.research_points = 0
        self.player_buildings = {}
        self.max_staff = 5

        #methods
        self.buildings = self.load_buildings(file_name)

        #init
        print(f"{player.name}'s factory initialised.")

    def add_building(self, building):
        #check self.cash > price
        if building in self.buildings:
            if building not in self.player_buildings:
                self.player_buildings[building] = 1
            else:
                self.player_buildings[building] += 1
        else:
            print("This is not a valid building")


    def hire_staff(self, staff):
        self.cash -= staff["Hire Cost"]
        #self.pay_staff(staff["Wage"])

    def load_buildings(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: file '{file_name} not found.'")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def menu(self):
        print(f"Welcome to your factory: {self.player.name}")
        print(f"Money {self.cash}")


        while True:
            print("1. View available buildings")
            print("2. Build new factories")
            print("3. Hire new staff.")
            print("4. Research")
            print("5. Factory data.")
            print("X. Exit")
        
            print("What would you like to do?")

            choice = input(">> ").upper()

            if choice == "1":
                for name, data in self.buildings.items():
                    print(f"{name} - ${data["Cost"]}. Input: {[i for i in data["Upkeep"]]}")

            elif choice == "2":
                print("Factories: ")
                for name, data in self.buildings.items():
                    print(f"{name} - ${data["Cost"]}")
                print("Which one would you like to purchase?")
                factory_choice = input(">> ")
                self.add_building(factory_choice)

            elif choice == "5":
                print(f"Buildings: {self.player_buildings}")



            elif choice == "X":
                print("Saving game...")
                #save game
                return

            else:
                print("Not a valid option.")

    

    