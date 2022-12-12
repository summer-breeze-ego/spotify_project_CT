# run this file once to create database txt file with users and their default playlists
import re

# initiating constants
FILENAME = 'users_database.txt'

# function to initiate database
def init_db(filename: str) -> None:

    # writing to file initially
    with open(filename, 'w') as filewrite:

        song_list = ['song1', 'song2', 'song3', 'song4', 'song5']

        for i in range(0, 50):

            # write the username and corresponding list to the file
            filewrite.write(f"{str(i + 1)} = {str(song_list)}\n")
        
        filewrite.close()

# creating database file
init_db(FILENAME)

# testing reading from file
with open(FILENAME, 'r') as fileread:

    pattern = "(\w+) = (\w+)"

    for line in fileread:
        print(line)

        match = re.search(pattern, "srting = akhsbfviuasd")

        username = match.group(1)
        playlist = match.group(2)

        print(f"{username} listens to {str(playlist)}")