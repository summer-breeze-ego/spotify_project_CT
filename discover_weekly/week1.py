# code for week1

import random
from typing import Dict, List
import math

def find_position(playlist: List[str], start: int, end: int) -> int:
    """
    A partial function for the quicksort alghorithm, sorts the list by picking a pivot from the end of the list and finds the position of the pivot in the list.
    Returns the position of where the pivot was found.

    :param playlist: any list that needs to be sorted.
    :paran start: the starting point in the list.
    :param end: the ending point in the list.
    :return: the index of the pivot.
    """
    # a pivot picked from the end of the list.
    pivot = playlist[end]
    # i that is used as an index value.
    i = start - 1
    # For each song in the list, place all the songs that are smaller then the pivot to the left side.
    for j in range(start, end):
        if playlist[j] <= pivot:
            i += 1
            (playlist[i], playlist[j]) = (playlist[j], playlist[i])
    # Change the song on the end of the list.
    (playlist[i + 1], playlist[end]) = (playlist[end], playlist[i + 1])
    # return the new index.
    return i + 1
    
def quicksort(playlist: List[str], start, end):
    """
    The quicksort algorithm uses recursion to sort any list, by picking a pivot point placing everything smaller to the left and everything bigger to the right.
    Until the list is completely sorted.

    :param playlist: any list that needs to be sorted.
    :paran start: the starting point in the list.
    :param end: the ending point in the list.
    """
    # calls the function until start < end (aka list is sorted)
    if start < end:
        # finds the position of of the last song and returns a new index for the next pivot.
        piv = find_position(playlist, start, end)
        # recursively finds the position of the song thats on the next lower index.
        quicksort(playlist, start, piv - 1)
        # recursively finds the position of the song thats on the next higher index.
        quicksort(playlist, piv + 1, end)


def special_binary_search(playlist: List[str], user: List[str]) -> int:
    """
    Performs binary search on sorted list and returns the number of matching items are found between two given lists.
    :param playlist: a sorted list of songs
    :param user: a list of songs a user listened to.
    :return: the amount of songs that are found in both lists. 
    """
    # x as the number of songs that are found in the playlist.
    x: int = 0
    # Repeats for each song in user.
    for song in user:

        # l as the left boundary.
        l: int = 0
        # r as the right boundary.
        r: int = len(playlist) - 1
        
        while l <= r:
            # m as the floor value of the middle of l and r.
            m = math.floor((l + r) / 2)
            if song == playlist[m]:
                # if the song is found x += 1
                x += 1
                break
            elif song < playlist[m]:
                r = m - 1
            else:
                l = m + 1
    return x

def discover_weekly_1(user: List[str], playlists: List[List[str]]) -> List[str]:
    """
    Randomly picks 5 songs from a random playlist which has at least 3 songs
    the user has listened to and 3 songs he has not listened to.

    :param user: list of songs a user listened to.
    :param playlists: list of playlists.
    """
    recommended_playlists: List[List[str]] = []

    # iterating over stock playlists 
    for playlist in playlists:

        # initializing necessary variables
        start = 0 # beginning of list
        end = len(playlist) - 1 # end of list

        # calling quicksort on the current playlist to organise it
        quicksort(playlist, start, end)
        # binum as the number of listened songs in a playlist found with binary search.
        binum = special_binary_search(playlist, user)
        # new songs as a number of songs, if the user has less then 3 not listened songs, 
        # the playlist is not considered a recommended playlist.
        new_songs = len(playlist) - 3
        
        if binum >= 3 and binum <= new_songs:
            recommended_playlists.append(playlist)

    # a random index picked from recommended playlists
    if len(recommended_playlists) == 0:
        exit("No playlist for this person.\n")

    # chosing random playlist
    i = random.sample(recommended_playlists, k=1)[0] # empty range

    # getting 5 new songs
    discover_weekly = random.sample(i, k=5)

    return discover_weekly
