from factory import Factory
from player import Player

if __name__ == "__main__":
    #player_name = input("Hey player, please enter your name: ")
    new_player = Player("Fabian")
    new_factory = Factory(new_player)

    new_factory.menu()