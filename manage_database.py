# run this file once to create database txt file with users and their default playlists
import re
import ast
from typing import Dict, List
import fileinput

# initiating needed constants
FILENAME = 'users_database.txt'

# function to initiate database
def init_db(filename: str, users: Dict[str, List[str]]) -> None:
    """Function initiates database of users and their initial playlists as text file.

    Args:
        filename (str): path to database file (existing or not)
        users (Dict[str, List[str]]): dictionary of users and their playlists.
    """

    # writing to file initially
    with open(filename, 'w') as filewrite:

        # looping through users
        for user in users:

            # write the username and corresponding list to the file
            filewrite.write(f"{user} = {users[user]}\n")
        
        filewrite.close()

# function to extract from text file database
def pull_db(filename: str) -> None:

    # testing reading from file
    with open(FILENAME, 'r') as fileread:

        pattern = "(\w+) = (\[.*\])"

        for line in fileread:
            print(line)

            match = re.search(pattern, line)

            username = match.group(1) # gets username from database
            playlist = ast.literal_eval(match.group(2)) #transforms list from string to actual list

            print(f"user {username} listens to {str(playlist)}\n\n\n")

# create function to input new songs to certain line
# check if user exists and then edit line with updated list of songs
# also able to edit username?
def edit_user(filename: str, username: str) -> None:

    playlist = ['a', 'b', 'c']
    
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        # loop through lines of file
        for line in file:
            # check if the line starts with the right username
            if line.startswith(str(username)):
                # replace the playlist with the updated playlist
                line = re.sub(r"{} = .*".format(username), "{} = {}".format(username, playlist), line)
            
            print(line, end='')
