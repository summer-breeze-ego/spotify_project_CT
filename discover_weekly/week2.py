# Week 2 - Genres

# imports
import random # Importing random for number generation
import csv # Import and opening CSV with data
from typing import Tuple, Dict, List

import os
os.chdir("/Users/augustincoman/Empire/Programming/spotify_project_CT")

# constants
CSV_FILE_NAME = "data/spotify-dataset.csv" # path to csv file

def get_genre() -> Tuple[List[str]]:
    """Function returns a tuple of lists of of songs split by genre.

    Returns:
        Tuple[str]: a tuple of song lists.
    """
    
    # initiating variables to store songs based on genres
    pop = []
    rock = []
    techno = []

    # managing files
    with open(CSV_FILE_NAME) as csvfile:
        csvreader = csv.reader(csvfile)
        
        next(csvreader)
        
        for row in csvreader:
            
            # Going through all songs in CSV file if certain words are in the genre, then record name in respective var
            # First pop, only need one if statement since pop is a large genre
            if "pop" in row[2]:
                pop.append(row[0])
                
            # Next rock and band for rock songs
            if "rock" in row[2]:
                rock.append(row[0])
            if "band" in row[2]:
                rock.append(row[0])
                
            # Lastly techno and electr for techno songs
            if "techno" in row[2]:
                techno.append(row[0])
            if "electr" in row[2]:
                techno.append(row[0])
        
    return pop, rock, techno

def discover_weekly_2(user_playlist: List[str]) -> List[str]:
    """Function takes user playlist and returns 5 new songs based on genre.

    Args:
        user_playlist (List[str]): user's songs.

    Returns:
        List[str]: list of 5 songs.
    """

    # initiating genres
    pop, rock, techno = get_genre()
    
    # initiating playlist of new songs
    discover_weekly = []

    popc = 0
    rockc = 0
    technoc = 0

    # looping through user songs to count how many for each genre
    for song in user_playlist:
        if song in pop:
            popc += 1
        if song in rock:
            rockc += 1
        if song in techno:
            technoc += 1

    # if the dominating genre is pop
    if popc > rockc and popc > technoc:

        # if there's at least one rock song we add another one and then most are pop
        if rockc >= 1:
            discover_weekly = random.sample(pop, k=4)
            discover_weekly.extend(random.sample(rock, k=1))
            return discover_weekly

        # same with techno and pop
        if technoc >= 1:
            discover_weekly = random.sample(pop, k=4)
            discover_weekly.extend(random.sample(techno, k=1))
            return discover_weekly

        discover_weekly = random.sample(pop, k=5)

    # if the dominating genre is rock
    if rockc > popc and rockc > technoc:

        # now with pop and rock
        if popc >= 1:
            discover_weekly = random.sample(rock, k=4)
            discover_weekly.extend(random.sample(pop, k=1)[0])
            return discover_weekly

        # now with techno and rock
        if technoc >= 1:
            discover_weekly = random.sample(rock, k=4)
            discover_weekly.extend(random.sample(techno, k=1))
            return discover_weekly

        discover_weekly.append(random.sample(rock, k=5))

    # if the dominating genre is techno
    if technoc > popc and technoc > rockc:

        # same with pop and techno
        if popc >= 1:
            discover_weekly = random.sample(techno, k=4)
            discover_weekly.extend(random.sample(pop, k=1))
            return discover_weekly

        # same with rock and techno
        if rockc >= 1:
            discover_weekly = random.sample(techno, k=4)
            discover_weekly.extend(random.sample(rock, k=1))
            return discover_weekly

        discover_weekly = random.sample(techno, k=5)
    
    return discover_weekly
