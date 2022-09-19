from BlackJack_classes import *
from BlackJack_funcs import *

def main():
    intro()
    player_list = init_players()        # creates player list
    insert_bets(player_list)            # prompts players to buy in
    deck = construct_deck()             # creates a deck of cards
    
if __name__ == "__main__":
    main()