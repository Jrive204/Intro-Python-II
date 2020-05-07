from room import Room
import time
import linecache
from os import system, name 
import asyncio


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# # Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
async def welcome():
    system('clear') 
    time.sleep(1)
    welcome = [linecache.getline('src/story.txt',2),
    linecache.getline('src/story.txt',3),linecache.getline('src/story.txt',5),
    linecache.getline('src/story.txt',7),linecache.getline('src/story.txt',8),
    linecache.getline('src/story.txt',10),
    linecache.getline('src/story.txt',12),]
    linecache.clearcache()
    for i in welcome:
        time.sleep(1)
        print(i)
    print("Fear sets in, your next response is Crucial... The wrong choice and its all over \n")
    print(' Act Tough and attempt to break the door down - [n]\n', "Beg for my life - [w]\n", "Ask about the game and play along for now - [e]\n", "Refuse to play at any cost - [s]\n ")

# welcome()

asyncio.run(welcome())


time.sleep(1)

while True:
    directions = {'n':"n","w":"w","e":"e","s":"s"}
    choices=f"How are you going to Approach this situations?? answers allowed {directions['n'],directions['w'],directions['e'],directions['s']} Type q to Exit the game\n"
    move= input(choices)
    
    
    
    try:
        if move == "q":
            print("Bye")
            time.sleep(1)
            break
        
        if move == "n":
            print("You tell the Voice it can go $%@# itself and begin kicking the door\n", "Gas starts seeping in, and the door isn't budging . .  .")
            time.sleep(1)
            break

        if move == "w":
            print("You Beg for your Life, you begin talking about your family and how they need you...\n", "The door opens .. I am outside")
            room['outside'].move()
            # break

        if move == "e":
            print("Not a valid response, Please Read What is Allowed!!! ")
            time.sleep(1)             
            # break

        if move == "s":
            print('S')
            time.sleep(1)
            # break 
    
        directions[move]

    except KeyError:
                print("Not a valid response, Please Read What is Allowed!!! ")
                time.sleep(1)

    # except ValueError:
    #      print("Hello")
    

