from extra_functions import *
from constants import *
from week1 import *
from week2 import *
from week3 import *

# main python file

# testing week1 code
for user in DEFAULT_USERS:

    # getting result playlist from week 1
    discover_weekly = discover_weekly_1(DEFAULT_USERS[user], DEFAULT_PLAYLISTS)

    # printing results
    print(f"For user {user} we got the following playlist: \
        {list(song for song in discover_weekly)}")
    
    # trial for push/pull