import sys

dataset = []
for i in range(1, 101):
    dataset.append(str(i))

songs = []
for i in range(1, 605):
    songs.append(str(i))

# amount of songs per playlist
N = 50

total_playlists = 100

# amount of default playlists
aodp = len(songs) // N

print(aodp)

if aodp < 12:
    sys.exit("not enonugh playlists")

# creating the first default playlists
for i in range(0, aodp):
    print("cock-a-doodle-doo")
