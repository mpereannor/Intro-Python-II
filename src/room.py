# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
  def __init__(self, name, description): 
    self.name = name 
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
    # self.item = Item
    
    
    
  def __str__(self):
    info = ''
    info  += f'{self.name} \n{self.description} \n'
    return info
  
  