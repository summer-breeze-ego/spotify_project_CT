import csv
import random
from typing import Dict, List
import re
# constants
SEED = 111 # seed for playlists forming

# defining "random" seed  - original = 111
random.seed(SEED)
csv_path = 'data/spotify-dataset.csv'

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

shifts()


# function to recommend 5 songs to each user 
def recommendation_shifts(filename: str):

  users = open(filename)
  happy = shifts()
  party = shifts()
  calming = shifts()
  lounge = shifts()
  
  for user in users:
    print(user)
    count_happy = 0
    count_party = 0
    count_calming = 0
    count_lounge = 0

    start = user.rfind("[")
    end = user.rfind("]")
    user = user.replace("'", "")
    user = user[start +1: end].split(",")
      
    for happy_song in happy:
      for song in user:
        if song == happy_song:
          count_happy += 1

    for party_song in party:
      for song in user:
        if song == party_song:
          count_party += 1

    for calming_song in calming:
      for song in user:
        if song == calming_song:
          count_calming += 1

    for lounge_song in lounge:
      for song in user:
        if song == lounge_song:
          count_lounge += 1

    rate_happy =  (count_happy / len(user)) * 100
    rate_party = (count_party / len(user) ) * 100
    rate_calming = (count_calming / len(user) ) * 100
    rate_lounge = (count_lounge / len(user) ) * 100

  return rate_happy, rate_party, rate_calming, rate_lounge

recommendation_shifts()
