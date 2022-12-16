import csv
import random
from typing import Dict, List
import re

def pull_user(filename: str, username: str) -> List[str]:
    """Function returns list of username's playlist from filename database.

    Args:
        filename (str): filename for database.
        username (str): user name.
    """

    # managing database
    with open(filename, 'r') as file:

        pattern = "(\w+) = (\[.*\])"

        # for each line in the file
        for line in file:

            print(line)

            # strip of newline
            line.rstrip()

            # if the line starts with the given username
            if line.startswith(str(username)):
                match = re.search(pattern, line)
                
                # getting user's playlist
                playlist = ast.literal_eval(match.group(2)) #transforms list from string to actual list
                
                return playlist
            
        exit("Error: no such user.")


# constants
SEED = 111 # seed for playlists forming

# defining "random" seed  - original = 111
random.seed(SEED)
csv_path = 'spotify-dataset.csv'

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

list_from_dataset(csv_path)

def shifts() -> List[str]:

  happy = []
  party = []
  calming = []
  lounge = []

  god_dataset = list_from_dataset(csv_path)

  for song in god_dataset:
    danceability = int(song[6])
    valence = int(song[9])
    energy = int(song[5])
    popularity = int(song[13])
    loudness = int(song[7])
    liveliness = int(song[8])
    acousticness = int(song[11])
    bpm = int(song[4])

    #Happy
    if danceability >= 50 and valence >= 50 and energy >= 50:
      happy.append(song[0])

    #Party
    if danceability >= 50 and energy >= 50 or popularity >=50 and loudness >= 50: #or bpm >= 140:
      party.append(song[0])

    #Calming
    if energy <= 50 and loudness <= 50 and acousticness <= 50:
      calming.append(song[0])

    #Lounge
    if energy <= 50 and loudness <= 50 and acousticness <= 50:
      lounge.append(song[0])

  #print(len(happy),len(party), len(calming), len(lounge))
  return happy
  return party
  return calming
  return lounge


# function to recommend 5 songs to each user 
def recommendation_shifts():

  file = open('users_database.txt')
  
  happy = shifts()
  party = shifts()
  calming = shifts()
  lounge = shifts()

  discover_weekly = []

  count_happy = 0
  count_party = 0
  count_calming = 0
  count_lounge = 0

  all_users = []

  for user in file:

    start = user.rfind("[")
    end = user.rfind("]")
    user = user.replace("'", "")
    user = user[start +1: end].split(",")

    for song in user:
      
      for happy_song in happy:
        if song == happy_song:
          count_happy += 1

      for party_song in party:
        if song == party_song:
          count_party += 1

      for calming_song in calming:
        if song == calming_song:
          count_calming += 1

      for lounge_song in lounge:
        if song == lounge_song:
          count_lounge += 1
    
    
      rate_happy =  (count_happy / len(user)) * 100
      rate_party = (count_party / len(user) ) * 100
      rate_calming = (count_calming / len(user) ) * 100
      rate_lounge = (count_lounge / len(user) ) * 100
    

      if rate_happy > rate_party and rate_happy > rate_lounge:

        if rate_lounge > rate_party:
          discover_weekly = random.sample(lounge, k=2)
          discover_weekly.extend(random.sample(happy, k=3))

        if rate_party > rate_lounge:
          discover_weekly = random.sample(party, k=2)
          discover_weekly.extend(random.sample(happy, k=3))

        discover_weekly = random.sample(happy, k=5)

      if rate_party > rate_happy and rate_party > rate_lounge:
        if rate_lounge > rate_happy:
          discover_weekly = random.sample(lounge, k=2)
          discover_weekly.extend(random.sample(party, k=3))

        if rate_happy > rate_lounge:
          discover_weekly = random.sample(happy, k=2)
          discover_weekly.extend(random.sample(party, k=3))

        discover_weekly = random.sample(party, k=5)

      if rate_lounge > rate_party and rate_lounge > rate_happy:
        if rate_happy > rate_party:
          discover_weekly = random.sample(happy, k=2)
          discover_weekly.extend(random.sample(lounge, k=3))

        if rate_party > rate_happy:
          discover_weekly = random.sample(party, k=2)
          discover_weekly.extend(random.sample(lounge, k=3))

        discover_weekly = random.sample(lounge, k=5)

      if rate_calming > 80 or rate_lounge > 80:
        discover_weekly = random.sample(calming, k=3)
        discover_weekly.extend(random.sample(lounge, k=2))
        
  return discover_weekly
recommendation_shifts()
