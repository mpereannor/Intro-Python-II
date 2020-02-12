from room import Room
from player import Player 
import textwrap

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
# treasure is key , Room instance is value 

# Link rooms together

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

avatar = Player('John Wick', 'male')
avatar.room = room['outside']

# Write a loop that:
for r in room:
# * Prints the current room name
  print(f'{room[r].name} \n')
# * Prints the current description (the textwrap module might be useful here).
  desc = room[r].description
  wrapper = textwrap.TextWrapper(width=10)
  print(wrapper.wrap(text=desc))
  print('___________')
  print('')
# * Waits for user input and decides what to do.
  
  #initialize
  choice = input('brave soul, move to your preferred room \n[n] ==> North\n[e] ==> East\n[s] ==> South\n[w] ==> West\n[q] ===> Quit\n' )
  current_room = room[r].name
  try:
    if current_room == 'outside':
      if choice == n_to:
        print('welcome to the Foyer!')
      # current_room += 1
        current_room + 1
      else:
        print("you can only head north")
        
    elif current_room == 'foyer':
      if choice == s_to:
        print("welcome to the outside")
        # current_room -= 1
        current_room - 1
      elif choice == n_to:
        print('welcome to the Overlook, watch your step')
        current_room + 1
      elif choice == e_to:
        print('welcome to the passage, watch your step')
        current_room + 2
      else:
        print("unfortunately you can not go west Columbus!")
        
    elif current_room == 'overlook':
      if choice == s_to:
        print("welcome to the Foyer!")
        current_room - 1
      else:
        print("you can only go south from this room")
        
    elif current_room == 'narrow':
      if choice == w_to:
        print('welcome to the Foyer!')
        current_room - 2
      elif choice == n_to:
        print('welcome to treasure room')
        current_room + 1
      else:
        print('you can only go west or north')
        
    elif current_room == 'treasure':
      if choice == s_to:
        print('welcome to the passage, watch your step')
        current_room - 1
      else:
        print('you can only go south from this room')
  else:
        print('game exiting')

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
