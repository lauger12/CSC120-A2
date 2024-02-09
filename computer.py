from typing import Optional

# create class Computer for all of our computer objects 
class Computer:

    # class attributes
   description: str 
   processor_type: str
   hard_drive_capacity: int
   memory: int
   operating_system: str
   year_made: int
   price: int

   # constructor for Computer class
   def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
   # methods
   # update price of computer to match the new price from refurbishment   
   def update_price(self, new_price:int):
         self.price = new_price    

   # update os of computer to match the new os from refurbishment   
   def update_os(self, new_os:str):
        self.operating_system = new_os

