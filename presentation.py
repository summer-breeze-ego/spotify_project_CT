# imports
from extra_functions import *
from constants import *
from discover_weekly.week1 import *
from discover_weekly.week2 import *
# from week3 import *

# testing week1 code
def week_1() -> None:
    """Print out all playlists from week 1.
    """
    for user in DEFAULT_USERS:

        # getting result playlist from week 3 - replace with week 3
        dw1 = discover_weekly_1(DEFAULT_USERS[user], DEFAULT_PLAYLISTS)

        print("\n----------------------------------------------------")
        print(f"For user {user} we got the following playlist:\n")
        for song in dw1:
            print(song)
        print("----------------------------------------------------\n")

# testing week 2 code
def week_2() -> None:
    """Print out all playlists from week 2.
    """

    for user in DEFAULT_USERS:

        # getting result playlist from week 3 - replace with week 3
        dw2 = discover_weekly_2(DEFAULT_USERS[user])

        print("\n----------------------------------------------------")
        print(f"For user {user} we got the following playlist:\n")
        for song in dw2:
            print(song)
        print("----------------------------------------------------\n")

# testing week 3 code
def week_3() -> None:
    """Print out all playlists from week 2.
    """

    for user in DEFAULT_USERS:

        # getting result playlist from week 3 - replace with week 3
        dw1 = discover_weekly_1(DEFAULT_USERS[user], DEFAULT_PLAYLISTS)

        print("\n----------------------------------------------------")
        print(f"For user {user} we got the following playlist:\n")
        for song in dw1:
            print(song)
        print("----------------------------------------------------\n")

# to see all names and according playlists
def all_users() -> None:
    """Print out all default playlists and users.
    """
    for user in DEFAULT_USERS:
         # printing users and playlists
        print("\n----------------------------------------------------")
        print(f"For user {user} we got the following playlist:\n")
        for i in DEFAULT_USERS[user]:
            print(i)
        print("----------------------------------------------------\n")


# chose what to see
choice = input("Choose what to see.\n[1] Discover Weekly 1\n[2] Discover Weekly 2\n[3] Discover Weekly 3\n[4] All default playlists\nYour choice:")

match choice:
    case '1':
        week_1()
    case '2':
        week_2()
    case '3':
        week_3()
    case '4':
        all_users()