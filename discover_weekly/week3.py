import csv
import random
from typing import List, Tuple


import os
os.chdir("/Users/augustincoman/Empire/Programming/spotify_project_CT")

CSV_FILE_NAME = 'data/spotify-dataset.csv'

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


def shifts() -> tuple[list[str]]:
	"""Categorizes all songs in 3 lists of 1 mood each.

	Returns:
		[tuple(List[str])]: 3 lists of songs as a tuple.
	"""

	# initiating lists of moods
	# we figure that calm and lounge are basically the same so we removed lounge
	happy = []
	party = []
	calming = []

	# get list of songs
	god_dataset = list_from_dataset(CSV_FILE_NAME)

	# for every song in the database
	for song in god_dataset:

		# getting initial data for each songs
		danceability = int(song[6])
		valence = int(song[9])
		energy = int(song[5])
		popularity = int(song[13])
		loudness = int(song[7])
		liveliness = int(song[8])
		acousticness = int(song[11])
		bpm = int(song[4])

		# if it's a happy song
		if danceability >= 50 and valence >= 50 and energy >= 50:
			happy.append(song[0])

		# if it's a party song
		if danceability >= 50 and energy >= 50 or popularity >=50 and loudness >= 50: #or bpm >= 140:
			party.append(song[0])

		# if it's a calming songs 
		if energy <= 50 and loudness <= 50 and acousticness <= 50:
			calming.append(song[0])

	return happy, party, calming

def discover_weekly_3(users_playlist: List[str]) -> List[str]:
	"""Generates discover weekly 3 songs based on incoming user playlist.

	Args:
		users_playlist (List[str]): list of user's songs.

	Returns:
		List[str]: list of discover weekly 3 songs.
	"""

	# getting mood shifts values from shifts() function
	happy, party, calming = shifts()

	# initiating discover_weekly result list
	discover_weekly = []

	# initiating mood counts
	count_happy = 0
	count_party = 0
	count_calming = 0

	# looping through songs in user's playlist
	# and counting the amount of songs per mood
	for song in users_playlist:
		# checking what mood it's in
		if song in happy:
			count_happy += 1
		if song in party:
			count_party += 1
		if song in calming:
			count_calming += 1
	
	# now it's time to calculate rating/ratio of every mood shift
	rate_happy =  (count_happy / len(users_playlist)) * 100
	rate_party = (count_party / len(users_playlist) ) * 100
	rate_calming = (count_calming / len(users_playlist) ) * 100
	
	# if rate_happy is dominant
	if rate_happy > rate_party and rate_happy > rate_calming:

		if rate_calming > rate_party:
			discover_weekly = random.sample(calming, k=2)
			discover_weekly.extend(random.sample(happy, k=3))

		elif rate_party > rate_calming:
			discover_weekly = random.sample(party, k=2)
			discover_weekly.extend(random.sample(happy, k=3))
		
		# if both then neither get picked
		else:
			discover_weekly = random.sample(happy, k=5)

	# if rate_party is dominant
	if rate_party > rate_happy and rate_party > rate_calming:
		if rate_calming > rate_happy:
			discover_weekly = random.sample(calming, k=2)
			discover_weekly.extend(random.sample(party, k=3))
		elif rate_happy > rate_calming:
			discover_weekly = random.sample(happy, k=2)
			discover_weekly.extend(random.sample(party, k=3))

		# if both then neither get picked
		else:
			discover_weekly = random.sample(party, k=5)

	# if rate_lounge is dominant
	if rate_calming > rate_party and rate_calming > rate_happy:
		
		# if rate_happy second place
		if rate_happy > rate_party:
			discover_weekly = random.sample(happy, k=2)
			discover_weekly.extend(random.sample(calming, k=3))
		
		# if rate_party second place
		elif rate_party > rate_happy:
			discover_weekly = random.sample(party, k=2)
			discover_weekly.extend(random.sample(calming, k=3))

		# if both then neither get picked
		else:
			discover_weekly = random.sample(calming, k=5)
			
	return discover_weekly