from Table import Table

if __name__ == "__main__":
    name = input('Welcome to Ironhack Blackjack table! Nice to have you here, please enter your name.\n')
    while not name:
        playerName = input('The input you submitted was invalid, please re-enter a valid name.\n')
    #In the start menu we could add more features in the future
    start_menu = int(input('What would you like to do?\n1 - Play\n2 - Exit '))
    if int(start_menu) == 1:
        table = Table(player_name=name)
        another_round = int(input('Would you like to play a round?\n1-Yes\n2-No\n'))
        #While the entry is not 0 we will keep playing rounds
        while another_round-2:
            table.play_round()
            while True:
                try:
                    another_round = int(input('Would you like to play a round?\n1-Yes\n2-No\n'))
                    break
                except TypeError:
                    print('There was an error in the entry please select option 1 or 2')
                except ValueError:
                    print('There was an error in the entry please select option 1 or 2')
    print('Thanks for playing in the Ironhack blacjack table, we hope you enjoyed your time here!')