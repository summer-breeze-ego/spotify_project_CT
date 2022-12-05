from typing import Dict, List

from extra_functions import *

import os
os.chdir("/Users/augustincoman/Library/CloudStorage/OneDrive-Personal/University/NL Courses/Period 2/Computational Thinking/Project Spotify")

# constants
CSV_FILE_NAME = "spotify-dataset.csv" # path to csv file
NR_PLAYLISTS = 100 # amount of default playlists
NR_USERS = 100 # amount of users (initially)

# getting data from csv file as list of lists
DATASET: List[str] = list_from_dataset(CSV_FILE_NAME)

# get default playlists from dataset
DEFAULT_PLAYLISTS: List[List[str]] = playlists_from_dataset(NR_PLAYLISTS, DATASET)

# getting names list
NAMES: List[str] = names()

# get default users and their initial playlist as dictionary 
DEFAULT_USERS: Dict[str, List[str]] = initial_users(NR_USERS, NAMES, DATASET)

# DEBUGGING

# debugging
i = 1
# for debugging
for playlist in DEFAULT_PLAYLISTS:
    print(f"playlist {i}:\n")
    print(playlist)
    print("\n")
    i+=1
