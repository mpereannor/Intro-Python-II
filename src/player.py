# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

  #composition 
class Player:
  def __init__(self, player_name):
    self.player_name = player_name
    self.current_room = None
    
    
