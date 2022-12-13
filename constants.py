# imports
from typing import Dict, List
from extra_functions import *

# import os
# os.chdir("/Users/augustincoman/Library/CloudStorage/OneDrive-Personal/University/NL Courses/Period 2/Computational Thinking/Project Spotify")

# constants
CSV_FILE_NAME = "spotify-dataset.csv" # path to csv file
NR_PLAYLISTS = 100 # amount of default playlists
NR_USERS = 100 # amount of users (initially)
INSTRUCTIONS = "\nINSTRUCTIONS\n1. Read everything carefuly.\n2. Respong to multiple choice questions with a number from 1 to 3 (or 'y' for yes and 'n' for no)\nand one or more words otherwise.\n3. Any unrecognised input will lead to an error and/or the termination of the program.\n4. To quit the program at any of the options steps just write something not available in the options.\n5. If you don't have an account or/and you're a new user you need to create a new account and then log in.\n"
FIRST_OPTION = [
    "[1] Understand the meaning of the App Name - Y KRAK.",
    "[2] New users: Choose an username and generate a random playlist for you.\n"
    "[3] Already have an account? Choose this."
]
NAME_EXPLAIN = "--------------------------------------------------\nY KRAK\nThe name KRACK comes an old tale of 5 student from VU Amsterdam who did a great job recreating Spotify's discover weekly.\nTheir initials were A, R, Y, K, K. Rearange that and you get << Y KRAK >>.\n\nIt was also speculated at the time of their demise that they all preferred Crack Cocaine over other drugs, which begged the question:\nWhy Crack\nIt was never confirmed by the creators, but the followers can only imagine what was going on inside their minds.\n--------------------------------------------------\n"
SECOND_OPTION = [
    "[1] Discover weekly 1",
    "[2] Discover weekly 2",
    "[3] Discover weekly 3"
]

# getting data from csv file as list of lists
DATASET: List[str] = list_from_dataset(CSV_FILE_NAME)

# get default playlists from dataset
DEFAULT_PLAYLISTS: List[List[str]] = playlists_from_dataset(NR_PLAYLISTS, DATASET)

# getting names list
NAMES: List[str] = names()

# get default users and their initial playlist as dictionary 
DEFAULT_USERS: Dict[str, List[str]] = initial_users(NR_USERS, NAMES, DATASET)

# DEBUGGING

# print(DEFAULT_USERS)
'''
i = 1

# for debugging
for playlist in DEFAULT_PLAYLISTS:
    print(f"playlist {i}:\n")
    print(playlist)
    print("\n")
    i+=1
'''