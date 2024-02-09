# Import the functions from computer and oo_resale_shop modules
from computer import * 
from oo_resale_shop import *


def main():
    # Create a ResaleShop class object called resalestore to represent our store
    resalestore =  ResaleShop()
    # Define computer_1 for main
    c1 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1000) #call Computer(...) constructor to create new computer instance

    # Print the computer resale store banner
    print("-" * 31)
    print("LOG IT! - COMPUTER RESALE STORE")
    print("-" * 31)

    # Buy a computer and add it to Resale Store inventory
    print("Item to buy:", resalestore.get_description(c1))
    resalestore.buy(c1)
    print("Adding to inventory...")
    print("Done.\n")

    #check inventory
    print("Checking inventory...")
    resalestore.print_inventory()
    print("Done.\n")

    # Refurbish computer
    print("Refurbishing item:", resalestore.get_description(c1))
    resalestore.refurbish(c1)
    print("Updating inventory...")   
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resalestore.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Item to sell:", resalestore.get_description(c1))
    resalestore.sell(c1)
    print("Done.\n")
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resalestore.print_inventory()
    print("Done.\n")

#Calls the main() function when this file is run
if __name__ == "__main__": 
    main()
