import pydealer as pd
from BlackJack_classes import *

def get_num_players():
    num_players = 0
    while num_players <= 0:

        try:
            num_players = int(input("How many players will be playing today?: "))
            if num_players <= 0:
                raise ValueError
        except ValueError:
            print("ERROR: The entry needs to be a whole number!")
            
    return num_players

def init_players(num_players):
    player_list = []
    money = input("How much money should each player start with?: ")
    for i in range (0, num_players):
        player = Player(input("Player " + str(i+1) + "'s name: "), money)
        player_list.append(player)
    
    print("The following players are playing: ")
    for player in player_list:
        print(player.name)
