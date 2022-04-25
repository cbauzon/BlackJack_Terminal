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

def init_players():
    player_ready = False
    while (player_ready == False):
        num_players = get_num_players()

        player_list = []
        money = 0

        while money <= 0:
            try:
                money = int(input("How much money should each player start with?: "))
                if money <= 0:
                    raise ValueError
            except ValueError:
                print("ERROR: The entry has to be a whole number!")

        for i in range (0, num_players):
            player = Player(input("Player " + str(i+1) + "'s name: "), money)
            player_list.append(player)
    
        print("The following players are playing with ${money} each: ".format(money = money))
        for player in player_list:
            print(player.name)

        ans = input("Is this correct? (y/n): ")
        if ans == "y":
            player_ready = True
        elif ans == "n":
            player_ready = False
        else:
            print("ERROR: Not a valid input!")
    return player_list

def insert_bets(player_list):
    for player in player_list:
        bet = 0
        while (bet <= 0) or (bet > player.money):
            try:
                bet = int(input(str(player.name) + ", how much would you like to bet?: "))
                if (bet <= 0) or (bet > player.money):
                    raise ValueError
            except ValueError:
                print("ERROR: Not a valid input!")
        player.sub_money(bet)
        print(player.name + " now has $" + str(player.money))

def construct_deck():
    deck = pd.Deck()
    deck.shuffle()
    return deck







