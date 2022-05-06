from BlackJack_classes import *
from BlackJack_funcs import *

def main():
    player_list = init_players()
    insert_bets(player_list)
    deck = construct_deck()
    print(deck)

if __name__ == "__main__":
    main()



