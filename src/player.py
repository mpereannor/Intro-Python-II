# Write a class to hold player information, e.g. what room they are in
# currently.

# class Player: 
#   def __init__(self, player_name, room, gender):
#     self.player_name = player_name
#     self.room = room
#     self.gender = gender
    
#   def __str__(self):
#     player_info = ''
#     player_info += f'{self.player_name} \n{self.room}\n{self.gender}\n'
#     return player_info
  
  
  
# wick = Player('John Wick', 'Lobby', 'Male')

# print(wick)
  
#inheritance 
from room import Room

# class Player(Room): 
#   def __init__(self,name, description, player_name, gender):
#     super().__init__(name, description)
#     self.player_name = player_name
#     self.gender = gender
    
#   def __str__(self):
#     player_info = ''
#     player_info += f'{self.player_name} \n{self.name}\n {self.gender}\n'
#     return player_info
  
  
  #composition 
class Player:
  def __init__(self, player_name, gender):
    self.player_name = player_name
    self.gender = gender 
    self.room = Room 
  
 
  
  