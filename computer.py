from typing import Optional


# create class Computer for all of our computer objects 
class Computer:

    # Class attributes
   description: str 
   processor_type: str
   hard_drive_capacity: int
   memory: int
   operating_system: str
   year_made: int
   price: int

    #Constructor for Computer object
   def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
       self.description = description
       self.processor_type = processor_type
       self.hard_drive_capacity = hard_drive_capacity
       self.memory = memory
       self.operating_system = operating_system
       self.year_made = year_made
       self.price = price
    
    #Methods   
   def update_price(self, new_price:int):
         self.price = new_price    
   
   def update_os(self, new_os:str):
        self.operating_system = new_os
        
