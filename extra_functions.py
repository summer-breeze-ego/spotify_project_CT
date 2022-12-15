import csv
import random
from typing import Dict, List
import re

def list_from_dataset(csv_path: str) -> List[str]:
    """Takes a path to a csv file and returns a list of its rows as lists.

    Args:
        csv_path (str): csv file path

    Returns:
        List[str]: list of song details.
    """

    # step 0: open file
    csv_file = open(csv_path)

    # reading csv file
    dataset = csv.reader(csv_file)
    #print(type(dataset))

    # initialzing csv data list
    god_dataset = []

    # add songs to list variable
    # list of lists
    for item in dataset:
        god_dataset.append(item)

    # delete first row crap
    del god_dataset[0]

    return god_dataset

# return amount of playlist from list of songs
def playlists_from_dataset(p_len: int, dataset: List[List[str]]) -> List[List[str]]:
    """Function returns p_len amount of playlists of random songs from dataset as list of (play)lists.

    Args:
        p_len (int): amount of playlists
        dataset (List[List[str]]): dataset of songs

    Returns:
        List[List[str]]: list of playlists.
    """

    playlists = []

    # loop creating 100 random playlists
    while len(playlists) < p_len:

        # initializing new playlist as empty every loop
        new_playlist = []

        # loop that adds 50 songs to each playlist
        # until there's 50 different songs in the playlist
        while len(new_playlist) <= 50:

            # getting random int (for selecting song)
            rand_int = random.randint(0, len(dataset) - 1)

            # selecting random song
            new_song = dataset[rand_int][0]

            # can't have same song twice in a playlist
            if new_song not in new_playlist:
                # adding song to playlist
                new_playlist.append(new_song)

        # at the end of every playlist loop
        # we append the new playlist to the list of playlists
        playlists.append(new_playlist)

    return playlists

# get names from file
def names() -> List[str]:
    """Generates list of names from txt file of names.

    Returns:
        List[str]: list of names.
    """

    names: List[str] = []

    # managing file
    try:
        # opening file
        file = open("/Users/augustincoman/Empire/Programming/spotify_project_CT/data/names.txt", 'r')
        
        # loop that appends names from file to names list
        for line in file:
            names.append(re.sub('\n', '', line))
            
    finally:
        # close file
        file.close() 

    return names

# get default users with 10 song playlists
def initial_users(nr_users: int, names: List[str], dataset: List[List[str]]) -> Dict[str, list[str]]:
    """Generates 100 users and their initial 10 song playlists.

    Arguments:
        [int]: amount of users.

    Returns:
        Dict[str, list[str]]: dictionary of users and initial list of songs.
    """

    # initialising dictionary of users
    users_dict = {}

    # loop until we fill the users dictionary
    while len(list(users_dict.keys())) < nr_users:
        
        # generate random name from names list
        name = random.choice(names)

        # if the name/user already is in the dictionary
        if name in list(users_dict.keys()):
            continue
    
        songs: List[str] = []

        for i in range(0, 10):
            # getting random int (for selecting song)
            rand_int = random.randint(0, len(dataset) - 1)

            # selecting random song
            new_song = dataset[rand_int][0]

            # can't have same song twice in a playlist
            if new_song not in songs:
                # adding song to playlist
                songs.append(new_song)

        users_dict[name] = songs

    return users_dict

# check if username is available
def username_is_available(filename: str, username: str) -> bool:
    # managing file
    with open(filename, 'r') as file:
        # loop through lines
        for line in file:
            # if the line starts with the username
            if line.startswith(f"{username} ="):
                return False # then username is not available
        
        file.close()
    
    return True

# function to confirm action
def confirmed() -> bool:
    """Function that asks user to confirm action.
    """

    confirmed = input("Write \"CONFIRM\" to confirm action.")

    if confirmed == "CONFIRM":
        return True
    else:
        return False

# for creating username
def create_username(filename: str) -> str:
    """Uses a loop to let the user chose an appropriate username and then returns it.

    Arguments:
        str: file where to store

    Returns:
        str: chosen username.
    """

    # initiate username
    username = input('What is your prefered username?')

    # looping until a valid username is chosen
    while True:
        # check if username is available
        if username_is_available(filename, username):
            if confirmed():
                print(f"Amazing username! Your account has been created!")
                break
            else:
                print("Username invalid.\n")

        username = input("Go ahead and choose another username")
        
    return username
