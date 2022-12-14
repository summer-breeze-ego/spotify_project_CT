# main python file

# imports
from extra_functions import *
from constants import *
from discover_weekly.week1 import *
from discover_weekly.week2 import *
# from discover_weekly.week3 import *
from manage_database import *

# database functions
# init_db(FILENAME, DEFAULT_USERS)
#pull_db(FILENAME)
#edit_user(FILENAME, 'Vanna')

# interacting with the user
# greeting
name = input("Hello! How may I adress you?\n")
print("What a lovely name, {}!".format(name))
print("Please read the instructions before proceeding any further.\n")
print(INSTRUCTIONS)
all_good = input("Do you understand everything? If not then you will have to restart the program. (y/n)")

if all_good != 'y':
    exit("Wow! Not enough brain cells I see. Buh bye, {}!".format(name))

# after instructions
print("Glad you're smart enough to comprehend a few sentences.\n\n\n------------------------------------\n          WELCOME TO Y KRAK\nYour soon to be favorite music streaming service.\n------------------------------------\n\n\nHow would you like to proceed?\n")

# loop for first three choices: title, create user, existing user (moves on)
while True:

    # listing options
    for n in range(0, len(FIRST_OPTION)):
        print(FIRST_OPTION[n])
    first_input = input('Your choice: ') # getting input

    # check if respone is valid
    if first_input not in ['1', '2', '3']:
        exit("Bruh. There's three options. Each row has a number at the beginning of the row. How ******* hard is it to chose one of those numbers.\nJesus ******* ******. {}? More like ******* *******.".format(name))

    # action based on user input
    match first_input:
        case '1': # 1
            print(NAME_EXPLAIN)

        case '2': # 2
            # managing username
            username = create_username(FILENAME) # call function to get user name
            print(f"You've chosen {username}.")
            add_user(FILENAME, username) # add user to database

            # manage playlist
            initial_playlist = initial_users(1, [username], DATASET)[username] # generate playlist for user
            print(initial_playlist) # for debugging
            print("Your account/playlist has been initiated.\n")
            edit_user(FILENAME, username, initial_playlist) # replace empty playlist with full one
        
        case '3': # input == first_input[2] (aka 3)
            # asking username
            username = input("What's your username?\nYour response: ")

            # username is not in database
            if username_is_available(FILENAME, username):
                print("\nThis username doesn't exist in our database.\n\n")
                continue

            # checks out
            print("\nChecks out!")
            break
            
        case _:
            exit("\nSomething ain't right, bruh, my bad...\nOr maybe you just wanted to quit...\n")
    
    print("\n\nAnyway... What would you like to do next?\n")

# now for discover weekly - the actual 
print("Now unto the interesting stuff.\n SPOTIFY WEEKLY\n")

# loop to simulate discover weekly for the user user
while True:
    # listing options
    for n in range(0, len(SECOND_OPTION)):
        print(SECOND_OPTION[n])
    second_input = input('Your choice: ') # getting input

    # action based on user input
    match second_input:
        case '1':
            # getting the dw1 playlist
            initial_playlist = pull_user(FILENAME, username)
            # print(type(initial_playlist))
            dw1_playlist = discover_weekly_1(initial_playlist, DEFAULT_PLAYLISTS)
            # print(type(dw1_playlist))
            # print(f"For {username} the first week playlist is {dw1_playlist}.")

            # managing the full playlist of old and new dw songs
            initial_playlist.extend(dw1_playlist)
            edit_user(FILENAME, username, initial_playlist)
            print("the full updated playlist is {}".format(initial_playlist))
        
        # second choice
        case '2':
            print("case 2")

        # third choice
        case '3':
            print("case 3")
        
        # default case
        case _:
            exit("\nSomething ain't right, bruh, my bad...\nOr maybe you just wanted to quit...\n")

    print("\n--------\ncoolio\n-------\n")
    break