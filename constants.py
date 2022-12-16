# imports
from typing import Dict, List
from extra_functions import *
'''
import os
os.chdir("/Users/augustincoman/Empire/Programming/spotify_project_CT")'''

# uncomment next line for same playlists and users
# random.seed(111)

# constants
CSV_FILE_NAME = "data/spotify-dataset.csv" # path to csv file
NR_PLAYLISTS = 100 # amount of default playlists
NR_USERS = 100 # amount of users (initially)
INSTRUCTIONS = "\nINSTRUCTIONS\n1. Read everything carefuly.\n2. Respong to multiple choice questions with a number from 1 to 3 (or 'y' for yes and 'n' for no)\nand one or more words otherwise.\n3. Any unrecognised input will lead to an error and/or the termination of the program.\n4. To quit the program at any of the options steps just write something not available in the options.\n5. If you don't have an account or/and you're a new user you need to create a new account and then log in.\n"
AFTER_INSTRUCTIONS = "Glad you're smart enough to comprehend a few sentences.\n\n\n------------------------------------\n          WELCOME TO WHITE COKE\nYour soon to be favorite music streaming service.\n------------------------------------\n\n\nHow would you like to proceed?\n"
FIRST_OPTION = [
    "[1] Understand the meaning of the App Name - WHITE COKE.",
    "[2] New users: Choose an username and generate a random playlist for you.",
    "[3] Already have an account? Choose this."
]
NAME_EXPLAIN = "--------------------------------------------------\nWHITE COKE\nWhat a great name. The names of the creators are Augustin, Kayran, Ruvan, Kornelija and Yunus. The initials are AKRKY.\nYou might have already noticed that it spells Y KRAK which can be read as White Crack.\nCrack aka Cocaine aka Coke which is how you get White Coke.\nWelcome to White Coke - so addicting it'll make your chest start hurting.\n--------------------------------------------------\n"
SPOTIFY_WEEKLY = "Now unto the interesting stuff.\n----------\n-- SPOTIFY WEEKLY\n----------\n"
SECOND_OPTION = [
    "[1] Discover weekly 1",
    "[2] Discover weekly 2",
    "[3] Discover weekly 3",
    "[4] Edit username"
]
FILENAME = 'data/users_database.txt'

# getting data from csv file as list of lists
DATASET: List[str] = list_from_dataset(CSV_FILE_NAME)

# get default playlists from dataset
DEFAULT_PLAYLISTS: List[List[str]] = playlists_from_dataset(NR_PLAYLISTS, DATASET)

# getting names list
NAMES: List[str] = names()

# get default users and their initial playlist as dictionary 
DEFAULT_USERS: Dict[str, List[str]] = initial_users(NR_USERS, NAMES, DATASET)

# DEBUGGING