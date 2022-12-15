# code for week1
# by Kayra Boelen

import random
from typing import Dict, List
import math

#playlists, 5 playlists from the dataset as sample
playlists = [['#Beautiful', 'A Little Party Never Killed Nobody (All We Got)', 'All of Me', 'Anywhere', 'Beautiful Birds (feat. Birdy)', 'Blurred Lines', "Can't Hold Us (feat. Ray Dalton)", 'Celebrate (From the Original Motion Picture "Penguins of Madagascar")', 'Champagne Problems', 'Cool Girl', 'Crazy Kids (feat. will.i.am)', 'Crying in the Club', 'Die Young', "Doesn't Mean Anything", 'Domino', 'Give Me Everything', 'Gorilla', 'Greenlight (feat. Flo Rida & LunchMoney Lewis)', 'Heartbreaker', 'Higher', 'Him & I (with Halsey)', 'Impossible', 'Just Can抰 Get Enough', 'Kills You Slowly', 'Kiss You', 'LIKE I WOULD', 'Let Her Go', 'Love The Way You Lie', 'Make Me... (feat. G-Eazy)', 'Mama', 'Never Be the Same - Radio Edit', 'Not About Angels', 'Not a Bad Thing', 'Overdose', 'Pep Rally', 'Praying', 'Right Now - Dyro Radio Edit', 'Rockabye (feat. Sean Paul & Anne-Marie)', "Runnin' (Lose It All)", 'Secrets', 'Send My Love (To Your New Lover)', 'Side To Side', 'Starving', 'Sucker', 'Supplies', 'The Edge Of Glory', 'The Greatest', 'Underneath the Tree', 'We Own The Night', 'When We Were Young', 'Your Love Is My Drug'], ['Love The Way You Lie', 'Blurred Lines', 'Just Can抰 Get Enough', 'The Edge Of Glory', 'Crying in the Club', 'Greenlight (feat. Flo Rida & LunchMoney Lewis)', 'Side To Side', 'The Greatest', 'Your Love Is My Drug', 'Gorilla', 'Kills You Slowly', 'Underneath the Tree', 'Mama', "Doesn't Mean Anything", 'Celebrate (From the Original Motion Picture "Penguins of Madagascar")', 'When We Were Young', "Runnin' (Lose It All)", 'Overdose', 'A Little Party Never Killed Nobody (All We Got)', 'Higher', 'Sucker', 'Heartbreaker', 'Give Me Everything', 'Champagne Problems', 'All of Me', 'Starving', 'Die Young', 'Anywhere', 'Secrets', 'Make Me... (feat. G-Eazy)', 'Right Now - Dyro Radio Edit', 'Impossible', 'Supplies', 'LIKE I WOULD', 'Not a Bad Thing', 'Rockabye (feat. Sean Paul & Anne-Marie)', 'Crazy Kids (feat. will.i.am)', 'Praying', 'Let Her Go', 'Never Be the Same - Radio Edit', 'Kiss You', 'Send My Love (To Your New Lover)', 'We Own The Night', 'Not About Angels', 'Cool Girl', 'Domino', 'Him & I (with Halsey)', 'Beautiful Birds (feat. Birdy)', 'Pep Rally', "Can't Hold Us (feat. Ray Dalton)", '#Beautiful'], ['Call You Mine', 'Kissing Strangers - Remix', 'Finally Found You', '...Ready For It? - BloodPop?Remix', 'We Are Here', 'Some Nights', 'Send My Love (To Your New Lover)', 'Love Never Felt So Good', "Messin' Around", "Stronger (What Doesn't Kill You)", 'Invitation', 'no tears left to cry', 'BURNITUP!', 'Wish That You Were Here - From 揗iss Peregrine抯 Home for Peculiar Children?Original Motion Picture', 'Starboy', 'Tired', 'This Is What You Came For', 'Mercy', 'Waves - Robin Schulz Radio Edit', 'Fireball (feat. John Ryan)', 'Mama', 'Kissing Strangers', 'OK - Spotify Version', 'Prayer in C - Robin Schulz Radio Edit', 'Next To Me', 'Happier', 'The Heart Wants What It Wants', 'We Are Never Ever Getting Back Together', 'Kill Em With Kindness', 'Live It Up', 'G.U.Y.', 'Let Me Go (with Alesso, Florida Georgia Line & watt)', '43776', 'Nothing Breaks Like a Heart (feat. Miley Cyrus)', "Please Don't Go", 'I Like It', 'Dangerous Woman', 'Grenade', 'Sugar (feat. Francesco Yates)', 'What About Love', 'Adore You', 'Set Fire to the Rain', 'Company', 'Body Say', 'A Little Party Never Killed Nobody (All We Got)', 'What Makes You Beautiful', 'Stay The Night - Featuring Hayley Williams Of Paramore', 'Born This Way', 'Locked Out of Heaven', 'Brave', 'My My My!'], ['Written in the Stars (feat. Eric Turner)', 'Love Me Like You Do - From "Fifty Shades Of Grey"', 'Atlas - From 揟he Hunger Games: Catching Fire?Soundtrack', 'Attention', 'Hands To Myself', '#thatPOWER', 'Nothing Breaks Like a Heart (feat. Miley Cyrus)', 'Alive', 'Call Me Maybe', 'Blow Me (One Last Kiss)', 'Beautiful Birds (feat. Birdy)', 'Wake Me Up', 'Sweet Nothing (feat. Florence Welch)', 'Rather Be (feat. Jess Glynne)', 'Lights - Single Version', 'Cannonball', 'Summertime Sadness (Lana Del Rey Vs. Cedric Gervais) - Cedric Gervais Remix', 'Bloodstream', 'Love On The Brain', 'Lose Yourself to Dance', 'Love Yourself', 'Stitches', 'Look What You Made Me Do', 'Something Just Like This', 'Cold (feat. Future)', 'What Do You Mean? - Acoustic', 'No Brainer (feat. Justin Bieber, Chance the Rapper & Quavo)', 'She Looks So Perfect', 'I Don抰 Wanna Live Forever (Fifty Shades Darker)', 'Want to Want Me', 'St Jude', 'Sick Boy', 'All I Ask', 'Problem', 'Just the Way You Are', 'Beneath Your Beautiful', 'Tee Shirt - Soundtrack Version', 'Blow', 'You Da One', 'Play Hard (feat. Ne-Yo & Akon) - New Edit', 'Best Thing I Never Had', 'Freak', 'Hey Mama (feat. Nicki Minaj, Bebe Rexha & Afrojack)', 'Rockabye (feat. Sean Paul & Anne-Marie)', 'Alejandro', 'Mi Gente (feat. Beyonc?', 'Young Girls', 'Let Me Love You', 'Uptown Funk', 'My My My!', 'You Lost Me'], ['Foolish Games', 'Firework', 'Tired', 'My Way', 'Animals', 'We Are Never Ever Getting Back Together', 'Spark The Fire', 'Same Old Love', 'Higher Love', 'Say Something', 'Next To Me', 'First Time', '43776', 'Super Bass', 'Good Time', 'I Love It (feat. Charli XCX)', 'What Makes You Beautiful', 'One Kiss (with Dua Lipa)', 'Cool Girl', 'human', 'I Took A Pill In Ibiza - Seeb Remix', 'Lemon', 'If I Had You', 'Little Lies', 'Written in the Stars (feat. Eric Turner)', 'Boyfriend', 'Confident', 'Run Run Run', 'Imma Be', 'Love Never Felt So Good', 'Antisocial (with Travis Scott)', 'Love', 'Ooh La La (from "The Smurfs 2")', "It Ain't Me (with Selena Gomez)", 'CAN\'T STOP THE FEELING! (Original Song from DreamWorks Animation\'s "TROLLS")', 'This Is How We Do', 'Slow Hands', 'Meet Me Halfway', 'My House', 'I Got You', 'Work', 'MOVE TO MIAMI', "There's Nothing Holdin' Me Back", 'Muny - Album Version (Edited)', 'Judas', 'Praying', '...Ready For It? - BloodPop?Remix', 'Impossible', 'Million Reasons', 'Give Me Everything', 'Get Low (with Liam Payne)']]
#users with random names and a playlist randomly picked from the dataset
users = {'Daniel': ['...Ready For It? - BloodPop?Remix', 'American Oxygen', 'Anything Could Happen', 'Applause', 'Bad Romance', 'Bang Bang', 'Beautiful Birds (feat. Birdy)', 'Blown', 'Body Say', 'Brave', 'Break Your Heart', 'Cannonball', 'Cruel (feat. ZAYN)', 'Do You Wanna Come Over?', "Doesn't Mean Anything", 'Dynamite', 'Hey Mama (feat. Nicki Minaj, Bebe Rexha & Afrojack)', 'I Luh Ya Papi', 'Jealous - Remix', 'Kissing Strangers - Remix', 'Latch', 'Let Me', 'Like A G6', 'Lips Are Movin', 'Little Lies', 'Mmm Yeah (feat. Pitbull)', 'NO', 'No Brainer (feat. Justin Bieber, Chance the Rapper & Quavo)', 'One Kiss (with Dua Lipa)', 'Only Love Can Hurt Like This', 'People Like Us', 'Pep Rally', 'Perfect', 'Reality - Radio Edit', 'Run Away With Me', 'Run the World (Girls)', 'Send My Love (To Your New Lover)', 'Slow Hands', 'Some Nights', 'Spark The Fire', 'Starving', 'Stereo Hearts (feat. Adam Levine)', 'Story of My Life', 'Take It Off', 'Tequila', 'There for You', 'Turn Up the Music', 'Water Under the Bridge', 'We Own The Night', 'Work Bitch', 'Yeah 3x'], 'Jack': ['3', 'All We Know', 'Beautiful People (feat. Khalid)', 'Best Song Ever', 'Blah Blah Blah (feat. 3OH!3)', 'Bloodstream', 'Born This Way', 'Break Free', 'Broken Arrows', 'Came Here for Love', "Can't Remember to Forget You (feat. Rihanna)", 'Cannonball', 'Castle Walls (feat. Christina Aguilera)', 'Close', 'Confident', "Doesn't Mean Anything", "Don't", 'Glad You Came', 'Good Time', 'Happier', 'Hello', 'I Lived', 'I Wanna Go', "I'm the One (feat. Justin Bieber, Quavo, Chance the Rapper & Lil Wayne)", 'Imma Be', 'Impossible', 'Just the Way You Are', 'Kissing Strangers', 'Lemon', 'Let Me Love You', 'Locked Out of Heaven', 'Marry You', 'Meet Me Halfway', 'Mr. Put It Down', 'One Call Away (feat. Tyga) - Remix', 'PILLOWTALK', 'Rock That Body', 'Sheezus', 'Silence', 'Starships', 'Story of My Life', 'Sucker', 'Take Back the Night', 'The Hills', 'The Time (Dirty Bit)', 'We Are Here', 'What Do You Mean? - Acoustic', 'Wiggle (feat. Snoop Dogg)', 'Words as Weapons', 'Yesterday (feat. Bebe Rexha)', "You're Mine (Eternal)"], 'Sylvie': ['Anaconda', 'Tee Shirt - Soundtrack Version', 'Mark My Words', 'Here', 'Picky - Remix', 'Bound To You - Burlesque Original Motion Picture Soundtrack', 'Get Low (with Liam Payne)', 'Girl On Fire (feat. Nicki Minaj) - Inferno Version', 'A Sky Full of Stars', 'Walk On Water (feat. Beyonc?', 'Downtown (feat. Melle Mel, Grandmaster Caz, Kool Moe Dee & Eric Nally)', 'Say Something', 'What I Need (feat. Kehlani)', 'Castle Walls (feat. Christina Aguilera)', 'LIKE I WOULD', 'No Guidance (feat. Drake)', 'Heartbeat Song', 'Love Me Like You Do - From "Fifty Shades Of Grey"', 'Despacito - Remix', 'Love Somebody', 'Alejandro', 'Paradise', 'Run Away With Me', 'Dance Again', 'Million Reasons', '...Ready For It? - BloodPop?Remix', 'Shape of You', 'I Know What You Did Last Summer', 'Youth (feat. Khalid)', "Runnin' (Lose It All)", 'Nervous', 'Bodak Yellow', 'We Are One (Ole Ola) [The Official 2014 FIFA World Cup Song]', 'Clown', 'Impossible', 'Tell Me You Love Me - NOTD Remix', "Really Don't Care", 'Love Never Felt So Good', 'Focus', 'Cruel (feat. ZAYN)', '#SELFIE', 'Closer', 'Live It Up', 'human', 'Strip That Down (feat. Quavo)', 'Sexy Bitch (feat. Akon)', "Don't Stop the Party (feat. TJR)", "There's Nothing Holdin' Me Back", 'Run the World (Girls)', 'Paris', 'Friends (with BloodPop?'], 'Andy': ['Foolish Games', 'Firework', 'Tired', 'My Way', 'Animals', 'We Are Never Ever Getting Back Together', 'Spark The Fire', 'Same Old Love', 'Higher Love', 'Say Something', 'Next To Me', 'First Time', '43776', 'Super Bass', 'Good Time', 'I Love It (feat. Charli XCX)', 'What Makes You Beautiful', 'One Kiss (with Dua Lipa)', 'Cool Girl', 'human', 'I Took A Pill In Ibiza - Seeb Remix', 'Lemon', 'If I Had You', 'Little Lies', 'Written in the Stars (feat. Eric Turner)', 'Boyfriend', 'Confident', 'Run Run Run', 'Imma Be', 'Love Never Felt So Good', 'Antisocial (with Travis Scott)', 'Love', 'Ooh La La (from "The Smurfs 2")', "It Ain't Me (with Selena Gomez)", 'CAN\'T STOP THE FEELING! (Original Song from DreamWorks Animation\'s "TROLLS")', 'This Is How We Do', 'Slow Hands', 'Meet Me Halfway', 'My House', 'I Got You', 'Work', 'MOVE TO MIAMI', "There's Nothing Holdin' Me Back", 'Muny - Album Version (Edited)', 'Judas', 'Praying', '...Ready For It? - BloodPop?Remix', 'Impossible', 'Million Reasons', 'Give Me Everything', 'Get Low (with Liam Payne)']}

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
        exit("No playlist for this person. Fuck them.\n")

    # chosing random playlist
    i = random.sample(recommended_playlists, k=1)[0] # empty range

    # getting 5 new songs
    discover_weekly = random.sample(i, k=5)

    return discover_weekly
