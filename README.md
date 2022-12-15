# spotify_project_CT

# What is this project
Coming soon...

# How to run the program
There are two main ways to run the program using the main.py file and the presentation one.

## 0. Before everything
If there is no text database file called something like "users_database.txt", first run the function 'init_db(filename, users_dict)' where filename is the name of the database and users_dict is a dictionary of usernames as keys and playlists as dictionaries.
You can either uncomment the line in the main.py file the first time you run it or straight up just do another python file, import the function and run it.

! in certain files (i.e., constants or week2) you might have to comment or change the os.chdir value. 

## 1. main.py
Using main.py it becomes a bit of a game. If you run it you can choose from multiple choices what to do at different steps, like creating a user, running one of the discover weekly algorithms on an existing one and seeing the meaning behind the name of the project.

## 2. presentation.py
Using presentation.py you can run one of the 3 discover weekly algorithms or just print all the default user-playlist duets..

# Introduction to the files
There are many files that this project is made of.

## 1. Database files
There are 4 database files in the ./data folder.

### 1.a names.txt
The names.txt files contains a ton of names that are used in this project to create default playlists.

### 1.b spotify-dataset.csv
The spotify dataset contains more than 600 songs that are used to create playlists and suggest new songs to users baed on the discover weekly algorithms.

### 1.c users_database.txt
A database for users and their playlists. This is where everything created through main.py is stored and/or changed.

### 1.d users_database.txt.bak
A backup for the 1.c database.

## 2. Discover Weekly files
The 3 main files containing the algorithms for the main 3 parts of the project.

### 2.a DW 1
The first one suggests 5 new songs to the user depending on their current playlist.

### 2.b DW 2
The second one suggests 5 songs based on the ratio of genres in the user's playlist.

### 2.c DW 3
The third one suggests songs based on the mood shifts represented by the user's past songs (or current playlist).

## 3. Auxiliary Files
There are a few files that contain variables and function to be used in the main two programs.

### 3.a constants.py
The constants.py file is a script that defines a multiple constants used to communicate with the user or just that are used along the algorithm.

### 3.b extra_functions.py
Contains numerous functions that help manage the database and define the constants in the constants file.

### 3.c manage_database.py
Contains the most important functions to manage the text file database.

## 4. Main programs
The two files that are used to run this project.

### 4.a main.py
Generates a game-like experience.

### 4.b presentation.py
Let's user show off the 3 discover weekly algorithms and the default users and their playlists.