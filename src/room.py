# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
  def __init__(self, name, description): 
    self.name = name 
    self.description = description
    
  def __str__(self):
    info = ''
    info  += f'{self.name} \n{self.description} \n'
    return info
  # def display_current_room:
  #   print(f'')
  #   room_name = ''
  # #   for 
  # #   for 
  
  '''
  * Create the REPL command parser in `adv.py` which allows the player to move to rooms
  in the four cardinal directions.
* Fill out Player and Room classes in `player.py` and `room.py`
'''