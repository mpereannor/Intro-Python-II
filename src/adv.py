from room import Room
from player import Player 

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

# avatar = Player('John Wick', 'male')
# avatar.room = room['outside']

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

avatar = Player(player_name)
avatar.current_room = room['outside']
# print(f'{current_room.name} \n')
# print(f'{current_room.description}\n')
print('___________')
print('')
  #initialize
print(f'Welcome {avatar.player_name}! you brave soul, move to your preferred room ')
choice = input(
  '[n] ==> North\n[e] ==> East\n[s] ==> South\n[w] ==> West\n[q] ===> Quit\n' )
while True:
# If the user enters a cardinal direction, attempt to move to the room there.
  try:
    if avatar.current_room == 'outside':
      if choice == 'n':
        print(f'welcome to the{avatar.current_room.name}!')
        print(f'welcome to the{avatar.current_room.description}!')
        avatar.current_room 
      else:
        print("you can only head north")
      
    elif avatar.current_room == 'foyer':
      if choice == 's':
        print("welcome to the outside")
        avatar.current_room 
      elif choice == 'n':
        print('welcome to the Overlook, watch your step')
        avatar.current_room 
      elif choice == 'e':
        print('welcome to the passage, watch your step')
        avatar.current_room 
      else:
        print("unfortunately you can not go west Columbus!")
      
    elif avatar.current_room == 'overlook':
      if choice == 's':
        print("welcome to the Foyer!")
        avatar.current_room 
      else:
        print("you can only go south from this room")
      
    elif avatar.current_room == 'narrow':
      if choice == 'w':
        print('welcome to the Foyer!')
        avatar.current_room 
      elif choice == 's':
        print('welcome to treasure room')
        avatar.current_room 
      else:
        print('you can only go west or north')
        
    elif avatar.current_room == 'treasure':
      if choice == 's':
        print('welcome to the passage, watch your step')
        avatar.current_room - 1
      else:
        print('you can only go south from this room')
# Print an error message if the movement isn't allowed.
  except ValueError:
      print('invalid selection, please try again ')

#
#
# If the user enters "q", quit the game.
