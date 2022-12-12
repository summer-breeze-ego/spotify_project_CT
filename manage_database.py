# run this file once to create database txt file with users and their default playlists
import re
import ast
from typing import Dict, List

# initiating needed constants
FILENAME = 'users_database.txt'

# function to initiate database
def init_db(filename: str, users: Dict[str, List[str]]) -> None:

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

pull_db(FILENAME)