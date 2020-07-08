from Table import Table

if __name__ == "__main__":
    name = input('Welcome to Ironhack Blackjack table! Nice to have you here, please enter your name.\n')
    while not name:
        playerName = input('The input you submitted was invalid, please re-enter a valid name.\n')
    start_menu = int(input('What would you like to do?\n1 - Play\n2 - See my scores '))
    if int(start_menu) == 1:
        table = Table(playerName=name)
        rounds_played = 0
        another_round = int(input('Would you like to play a round?\n0-No\n1-Yes\n'))
        while another_round:
            table.play_round()
    if start_menu == 2:
        print('PENDING TO BE DONE')
    print('Thanks for playing in the Ironhack blacjack table, we hope you enjoyed your time here!')