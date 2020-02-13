# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
# from item import Item
 
class Player:
  def __init__(self, player_name, current_room):
    self.player_name = player_name
    self.current_room = current_room
    # self.inventory = Item
  def define_player_room(self, current_room): 
    self.current_room = current_room
    
  def move_player(self, current_room):
    if current_room != None:
      self.define_player_room(current_room)
    else:
      print('not permitted to move in that direction from this room')
    
