import pydealer as pd
from BlackJack_classes import *

def get_num_players():
    num_players = "0"
    while num_players == "0":
        num_players = input("How many players will be playing today?: ")
        if num_players == "0":
            print("Not enough players. As many as 4 players can play")
    return int(num_players)

def init_players(num_players):
    player_list = []
    for i in range (0, num_players):
        pass