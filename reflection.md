Use this file to record your reflection on this assignment. 

What worked, what didn't, what advice would you give someone taking this course in the future?

Trying to go right into the code without a plan won’t end well. Writing out the pseudocode to give myself direction seriously helped! Furthermore, I got a notebook specifically for this class where I write out all my classes, objects, attributes, and functions, as well as drawing diagrams so I can better visually understand what exactly my program is doing, since I am still learning a lot about OOP and how to move data around! 

Not doing this at first, I was quickly getting overwhelmed, since was worried about my python skills and trying to look at all of the main code at once without a plan can be too much. So, I went back to drawing board, created a document with plans and functionalities I wanted for each class

Looking at other examples of OOP online, used in a variety of ways beyond this example, helped frame exactly how each class and object is able to be used outside of this assignment. 

I had a habit of jumping around from task to task at the start, but it can be much more useful if you have smaller goals within the project and check them off one at a time. Ex: defining computer attributes before working on defining the oop resale shop. Checking the procedural code for direction on what the program should do is also a big tip for anyone taking this course in the future. 

I also brainstormed that for the OS, I could use a list with all the Mac OS updates and progress the OS version up the list, but I realized that we are just updating to the newest OS, not advancing forward one update. Also – I didn’t want to risk using syntax I was too unfamiliar with which could cause bugs later on (at least for something that wasn’t even going to be needed functionally in the program).

For what didn’t work, I was having issues with the print function returning memory locations instead of a string. I was eventually able to figure this out by creating a function in ResaleShop:

def get_description(self, computer):
      return computer.description

so that I could return the computer description in main. I was also able to get the inventory list to print.

For what did work, I was able to define the methods and attributes for Computer and oo_Resale_Shop and call objects from Computer into the Resale Shop and successfully create instances of the Computer object. I was able to successfully run the functions in a rewritten main as well! 

I went to TA hours, which were very helpful! Talking through with the TAs helped me find and fix bugs in my code and strengthen my understanding of OOP.

Overall, I think this assignment has really helped me begin to understand OOP. And while there were roadblocks and many points of confusion, by the end I think I've made progress since when I started A2. :D