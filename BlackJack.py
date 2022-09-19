from BlackJack_classes import *
from BlackJack_funcs import *

def main():
    intro()
    player_list = init_players()
    insert_bets(player_list)

if __name__ == "__main__":
    main()
    #player = Player("CJ", 500)
    #print(player)