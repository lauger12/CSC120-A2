from typing import Optional
from computer import * 

# create class ResaleShop for all resale shops (this project will only have one store)
class ResaleShop:
    # constructor for ResaleShop class
    def __init__(self):
        self.inventory = [] #create inventory as a list  
        
    #functions
    
    # returns computer description, this is for returning in strings for main.py to show which computer is being acted upon for buying, selling, refurbishment, etc
    def get_description(self, computer):
      return computer.description
    
    # buy function, adds computer to inventory
    def buy(self, computer):
      self.inventory.append(computer) #call inventory append to add the new Computer instance to inventory
      print("Buying", computer.description + "...")

    # sell function, removes computer from inventory
    def sell(self, computer:Computer):
        if computer in self.inventory:
            print("Selling", computer.description + "...")
            self.inventory.remove(computer)
            print("Item", computer.description, "has been sold!")
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.")
    
    # function to print the current inventory
    def print_inventory(self):
        if self.inventory:  
            for comp in self.inventory:
                print(comp.description, ",", comp.processor_type, ",", comp.hard_drive_capacity, ",", comp.memory, ",", comp.operating_system, ",", comp.year_made, ",", comp.price)
        else:
            print("No inventory to display.")
    

    # code for refursbishing, updates price based on year and updates OS if the computer's OS not the most recent OS (new_OS)
    def refurbish(self, new_os:Optional[str] = None):
        new_os = "MacOS Monterey" 
        for comp in self.inventory:
                if comp.year_made < 2000:
                    comp.price = 0 # too old to sell, donation only
                elif comp.year_made < 2012:
                    comp.price = 250 # heavily-discounted price on machines 10+ years old
                elif comp.year_made < 2018:
                    comp.price = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    comp.price = 1500 # recent stuff
            
                if new_os is not None: 
                    comp.operating_system = new_os # update details after installing new OS
                else:
                    print("Item", comp.description, "not found. Please select another item to refurbish.")


#Test code for refurbishing, disregard in final
# def main():
#         resalestore =  ResaleShop()
#         c1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS High Sierra", 2014, 500) #call Computer(...) constructor to create new computer instance
        
#         resalestore.buy(c1)
#         resalestore.print_inventory()
#         resalestore.refurbish(c1)
#         resalestore.print_inventory()

    
# main()