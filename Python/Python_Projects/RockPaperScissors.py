import random

# Function to define the game rules
def rules(user_input):

    # Caseless
    user_input = user_input.casefold()
    # If Not Exit keep playing
    while(user_input != ('Exit').casefold()):
        user_input = user_input.casefold()
        # System generates random input choice
        choice = (str(random.choice(['Rock', 'Paper', 'Scissor']))).casefold()

        # If system input and user input are same play again
        if(user_input == choice):
            user_input = input(f' {choice}. \n\nPlease enter again: ')
            continue

        # Rules
        elif ((user_input == ('Rock').casefold() and choice == ('Paper').casefold())
            or (user_input == ('Scissor').casefold() and choice == ('Rock').casefold())
            or (user_input == ('Paper').casefold() and choice == ('Scissor').casefold())):
            user_input = input(f" {choice} You Lost. \n\nPlease enter again: ")
            continue

        elif ((user_input == ('Paper').casefold() and choice == ('Rock').casefold())
            or (user_input == ('Rock').casefold() and choice == ('Scissor').casefold())
            or (user_input == ('Scissor').casefold() and choice == ('Paper').casefold())):
            user_input = input(f" {choice} You Win. \n\nPlease enter again: ")
            continue

        # If invalid input enter again
        else:
            user_input = input("\n\nError: Please enter valid input (Rock/Paper/Scissor): ")
            continue


# Begin the game
print('ROCK PAPER SCISSOR\nGAME STARTED\n')
# Take user input
usr_in = input('Please enter your choice. (Rock/Paper/Scissor): ')
# Function call
rules(usr_in)
