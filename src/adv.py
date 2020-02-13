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
# If the user enters "q", quit the game.

# Print an error message if the movement isn't allowed.
# print(f'{current_room.name} \n')
# print(f'{current_room.description}\n')
# If the user enters a cardinal direction, attempt to move to the room there.

  #initialize
  
  
  
  
avatar = Player('Chuck Norris', room['outside'])
choice = ''
success = input(f'Welcome! {avatar.player_name}, You are currently in {avatar.current_room} move to your preferred room... Press Enter...')
while True:
  print(f'hello {avatar.player_name}, you are currently in {avatar.current_room} move to you preferred room.')
  choice = input( 'Hey, kindly choose your direction [n] ==> North\n[e] ==> East\n[s] ==> South\n[w] ==> West\n[q] ===> Quit\n' )
  
  current_room = avatar.current_room
  if choice == 'n':
    print('you choose the north ')
    next_room = avatar.current_room.n_to
    avatar.move_player(next_room)
  elif choice == 's':
    print('you choose the south, bold choice')
    next_room = avatar.current_room.s_to
    avatar.move_player(next_room)
  elif choice == 'e':
    print('you choose the east, ....okay!')
    next_room = avatar.current_room.e_to
    avatar.move_player(next_room)
  elif choice == 'w':
    print('you choose the west, NOOICE!')
    next_room = avatar.current_room.w_to
    avatar.move_player(next_room)
  elif choice == 'q':
    print('bye')
    break
  else:
    error = 'invalid input'
    print(error)
    
    


































#previous attempt
'''
player_name = input(f'Welcome! you brave soul,  enter your name ' )
avatar = Player(player_name, room['outside'])
position = avatar.room
success = input(f'Welcome! {avatar.player_name}, You are currently in {position.name} move to your preferred room... Press Enter...')
choice = ''
while choice == '':
  choice = input(
    '[n] ==> North\n[e] ==> East\n[s] ==> South\n[w] ==> West\n[q] ===> Quit\n' )
  try:
    
    if choice == 'n':
      if avatar ==  Player(player_name, room['outside']):
         avatar = Player(player_name, room['outside'].n_to)
         print(f'welcome to the {avatar.room}!')
         choice = ''
          
      elif avatar ==  Player(player_name, room['foyer']):
        avatar = Player(player_name, room['foyer'].n_to)
        print(f'welcome to the {avatar.room}!')
        # print(f'{position.description}!')
        choice = ''
      elif avatar ==  Player(player_name, room['narrow']):
        avatar = Player(player_name, room['narrow'].n_to)
        print(f'welcome to the {avatar.room}!')
        choice = ''
           
    elif choice == 's':
      if position == room['foyer']:
        position.s_to
        print(f'welcome to the {position.name}!')
        print(f'{position.description}!')
        choice = ''
      elif position == room['treasure']:
        position.s_to
        print(f'welcome to the {position.name}!')
        print(f'{position.description}!')
        choice = ''
      else: 
        print('wrong choice try again')
        choice = ''
    
    elif choice == 'e':
      if position == room['foyer']:
        position.e_to
        print(f'welcome to the {position.name}!')
        print(f'{position.description}!')
        choice = ''
        
    elif choice == 'w':
      if position == room['narrow']:
        position.w_to
        print(f'welcome to the {position.name}!')
        print(f'{position.description}!')
        choice = ''
    
    elif choice == 'q':
      print(f'exiting game {avatar.player_name}')

    else:
      print('invalid selection, please try again')
      choice = ''
  except TypeError:
    print('try again')
    choice= ''
   ''' 