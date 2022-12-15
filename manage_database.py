# run this file once to create database txt file with users and their default playlists
import re
import ast
from typing import Dict, List
import fileinput

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
    """Print all playlists from filename.

    Args:
        filename (str): filename.
    """

    # testing reading from file
    with open(filename, 'r') as fileread:

        pattern = "(\w+) = (\[.*\])"

        for line in fileread:

            match = re.search(pattern, line)

            username = match.group(1) # gets username from database
            playlist = ast.literal_eval(match.group(2)) #transforms list from string to actual list

            print(f"user {username} listens to {str(playlist)}\n\n\n")

# to get a certain user's playlist
def pull_user(filename: str, username: str) -> List[str]:
    """Function returns list of username's playlist from filename database.

    Args:
        filename (str): filename for database.
        username (str): user name.
    
    Returns:
        List[str]: list of songs of user.
    """

    # managing database
    with open(filename, 'r') as file:

        pattern = "(\w+) = (\[.*\])"

        # for each line in the file
        for line in file:

            # strip of newline
            line.rstrip()

            # if the line starts with the given username
            if line.startswith(str(username)):
                match = re.search(pattern, line)
                
                # getting user's playlist
                playlist = ast.literal_eval(match.group(2)) #transforms list from string to actual list
                
                return playlist
            
        exit("Error: no such user.")

# create function to input new songs to certain line
# check if user exists and then edit line with updated list of songs
# also able to edit username?
def edit_user(filename: str, username: str, playlist: List[str]) -> None:
    """Function updates playlist for user given in the file given.

    Args:
        filename (str): file database
        username (str): username searched for
        playlist (List[str], optional): new playlist. Defaults to [].
    """
    
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        # loop through lines of file
        for line in file:
            # check if the line starts with the right username
            if line.startswith(str(username)):
                # replace the playlist with the updated playlist
                line = re.sub(r"{} = .*".format(username), "{} = {}".format(username, playlist), line)
            
            print(line, end='')

# to add new user to database
def add_user(filename: str, new_user: str) -> None:
    """Function adds provided user to provided file.

    Args:
        filename (str): database file
        new_user (str): username.
    """

    # managing file
    with open(filename, 'a') as file:
        # write initial username and empty list in the database
        file.write(f"\n{new_user} = []")

        file.close()

def edit_username(filename: str, username: str, new_username, playlist: List[str]) -> None:
    """The function edits a username

    Args:
        filename (str): path to database file.
    """

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        
        # loop through lines of file
        for line in file:

            # check if the line starts with the OG username
            if line.startswith(str(username)):

                # replace the old username with the new one
                line = line.replace(username, new_username)
            
            print(line, end='')