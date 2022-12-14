# Week 2 - Genres - Yunus Turer #


# Making variables to store data

fields = []
rows = []

pop = []
rock = []
techno = []

# Import and opening CSV with data
import csv

with open('spotify-dataset.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
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
# Example users var
#users = {'Daniel': ['...Ready For It? - BloodPop?Remix', 'American Oxygen', 'Anything Could Happen', 'Applause', 'Bad Romance', 'Bang Bang', 'Beautiful Birds (feat. Birdy)', 'Blown', 'Body Say', 'Brave', 'Break Your Heart', 'Cannonball', 'Cruel (feat. ZAYN)', 'Do You Wanna Come Over?', "Doesn't Mean Anything", 'Dynamite', 'Hey Mama (feat. Nicki Minaj, Bebe Rexha & Afrojack)', 'I Luh Ya Papi', 'Jealous - Remix', 'Kissing Strangers - Remix', 'Latch', 'Let Me', 'Like A G6', 'Lips Are Movin', 'Little Lies', 'Mmm Yeah (feat. Pitbull)', 'NO', 'No Brainer (feat. Justin Bieber, Chance the Rapper & Quavo)', 'One Kiss (with Dua Lipa)', 'Only Love Can Hurt Like This', 'People Like Us', 'Pep Rally', 'Perfect', 'Reality - Radio Edit', 'Run Away With Me', 'Run the World (Girls)', 'Send My Love (To Your New Lover)', 'Slow Hands', 'Some Nights', 'Spark The Fire', 'Starving', 'Stereo Hearts (feat. Adam Levine)', 'Story of My Life', 'Take It Off', 'Tequila', 'There for You', 'Turn Up the Music', 'Water Under the Bridge', 'We Own The Night', 'Work Bitch', 'Yeah 3x']}
users = {'Daniel': ['...Ready For It? - BloodPop?Remix', 'American Oxygen', 'Anything Could Happen', 'Applause', 'Bad Romance', 'Bang Bang', 'Beautiful Birds (feat. Birdy)', 'Blown', 'Body Say', 'Brave', 'Break Your Heart', 'Cannonball', 'Cruel (feat. ZAYN)', 'Do You Wanna Come Over?', "Doesn't Mean Anything", 'Dynamite', 'Hey Mama (feat. Nicki Minaj, Bebe Rexha & Afrojack)', 'I Luh Ya Papi', 'Jealous - Remix', 'Kissing Strangers - Remix', 'Latch', 'Let Me', 'Like A G6', 'Lips Are Movin', 'Little Lies', 'Mmm Yeah (feat. Pitbull)', 'NO', 'No Brainer (feat. Justin Bieber, Chance the Rapper & Quavo)', 'One Kiss (with Dua Lipa)', 'Only Love Can Hurt Like This', 'People Like Us', 'Pep Rally', 'Perfect', 'Reality - Radio Edit', 'Run Away With Me', 'Run the World (Girls)', 'Send My Love (To Your New Lover)', 'Slow Hands', 'Some Nights', 'Spark The Fire', 'Starving', 'Stereo Hearts (feat. Adam Levine)', 'Story of My Life', 'Take It Off', 'Tequila', 'There for You', 'Turn Up the Music', 'Water Under the Bridge', 'We Own The Night', 'Work Bitch', 'Yeah 3x'], 'Jack': ['3', 'All We Know', 'Beautiful People (feat. Khalid)', 'Best Song Ever', 'Blah Blah Blah (feat. 3OH!3)', 'Bloodstream', 'Born This Way', 'Break Free', 'Broken Arrows', 'Came Here for Love', "Can't Remember to Forget You (feat. Rihanna)", 'Cannonball', 'Castle Walls (feat. Christina Aguilera)', 'Close', 'Confident', "Doesn't Mean Anything", "Don't", 'Glad You Came', 'Good Time', 'Happier', 'Hello', 'I Lived', 'I Wanna Go', "I'm the One (feat. Justin Bieber, Quavo, Chance the Rapper & Lil Wayne)", 'Imma Be', 'Impossible', 'Just the Way You Are', 'Kissing Strangers', 'Lemon', 'Let Me Love You', 'Locked Out of Heaven', 'Marry You', 'Meet Me Halfway', 'Mr. Put It Down', 'One Call Away (feat. Tyga) - Remix', 'PILLOWTALK', 'Rock That Body', 'Sheezus', 'Silence', 'Starships', 'Story of My Life', 'Sucker', 'Take Back the Night', 'The Hills', 'The Time (Dirty Bit)', 'We Are Here', 'What Do You Mean? - Acoustic', 'Wiggle (feat. Snoop Dogg)', 'Words as Weapons', 'Yesterday (feat. Bebe Rexha)', "You're Mine (Eternal)"], 'Sylvie': ['Anaconda', 'Tee Shirt - Soundtrack Version', 'Mark My Words', 'Here', 'Picky - Remix', 'Bound To You - Burlesque Original Motion Picture Soundtrack', 'Get Low (with Liam Payne)', 'Girl On Fire (feat. Nicki Minaj) - Inferno Version', 'A Sky Full of Stars', 'Walk On Water (feat. Beyonc?', 'Downtown (feat. Melle Mel, Grandmaster Caz, Kool Moe Dee & Eric Nally)', 'Say Something', 'What I Need (feat. Kehlani)', 'Castle Walls (feat. Christina Aguilera)', 'LIKE I WOULD', 'No Guidance (feat. Drake)', 'Heartbeat Song', 'Love Me Like You Do - From "Fifty Shades Of Grey"', 'Despacito - Remix', 'Love Somebody', 'Alejandro', 'Paradise', 'Run Away With Me', 'Dance Again', 'Million Reasons', '...Ready For It? - BloodPop?Remix', 'Shape of You', 'I Know What You Did Last Summer', 'Youth (feat. Khalid)', "Runnin' (Lose It All)", 'Nervous', 'Bodak Yellow', 'We Are One (Ole Ola) [The Official 2014 FIFA World Cup Song]', 'Clown', 'Impossible', 'Tell Me You Love Me - NOTD Remix', "Really Don't Care", 'Love Never Felt So Good', 'Focus', 'Cruel (feat. ZAYN)', '#SELFIE', 'Closer', 'Live It Up', 'human', 'Strip That Down (feat. Quavo)', 'Sexy Bitch (feat. Akon)', "Don't Stop the Party (feat. TJR)", "There's Nothing Holdin' Me Back", 'Run the World (Girls)', 'Paris', 'Friends (with BloodPop?'], 'Andy': ['Foolish Games', 'Firework', 'Tired', 'My Way', 'Animals', 'We Are Never Ever Getting Back Together', 'Spark The Fire', 'Same Old Love', 'Higher Love', 'Say Something', 'Next To Me', 'First Time', '43776', 'Super Bass', 'Good Time', 'I Love It (feat. Charli XCX)', 'What Makes You Beautiful', 'One Kiss (with Dua Lipa)', 'Cool Girl', 'human', 'I Took A Pill In Ibiza - Seeb Remix', 'Lemon', 'If I Had You', 'Little Lies', 'Written in the Stars (feat. Eric Turner)', 'Boyfriend', 'Confident', 'Run Run Run', 'Imma Be', 'Love Never Felt So Good', 'Antisocial (with Travis Scott)', 'Love', 'Ooh La La (from "The Smurfs 2")', "It Ain't Me (with Selena Gomez)", 'CAN\'T STOP THE FEELING! (Original Song from DreamWorks Animation\'s "TROLLS")', 'This Is How We Do', 'Slow Hands', 'Meet Me Halfway', 'My House', 'I Got You', 'Work', 'MOVE TO MIAMI', "There's Nothing Holdin' Me Back", 'Muny - Album Version (Edited)', 'Judas', 'Praying', '...Ready For It? - BloodPop?Remix', 'Impossible', 'Million Reasons', 'Give Me Everything', 'Get Low (with Liam Payne)']}


user_five_songs = {}
# Importing random for number generation
import random

def userlabel(users):

    
    for key, values in users.items():
        popc = 0
        rockc = 0
        technoc = 0
        for value in values:
            if value in pop:
                popc += 1
            if value in rock:
                rockc += 1
            if value in techno:
                technoc += 1
        
        if popc > rockc and popc > technoc:
            user_five_songs[key] = random.sample(pop, k=5)
        if rockc > popc and rockc > technoc:
            user_five_songs[key] = random.sample(rock, k=5)
        if technoc > popc and technoc > rockc:
            user_five_songs[key] = random.sample(techno, k=5)
    print(user_five_songs)
            

        
userlabel(users)       
        
        

# List of users and songs that they have listened to prior to week 2


# There are only 3 types of categories for music
# Rock
# Pop
# Techno
# Assigning every song to one of these, else N/A




# Check which category is the highest percentage


# Mark that user as 'insert-category listener' and recommend 5 song