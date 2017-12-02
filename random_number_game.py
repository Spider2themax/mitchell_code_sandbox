import random
from array import*
lowest_number=int(raw_input("Enter a lower number to guess between: "))
highest_number=int(raw_input("Enter a upper number to guess between: "))
number_to_guess=random.randint(lowest_number,highest_number)
attempts=0
highest=highest_number
lowest=lowest_number
computer_guess=lowest_number
while(computer_guess!=number_to_guess):
   print computer_guess
   attempts=attempts+1
   if computer_guess<number_to_guess:
      lowest=computer_guess
      computer_guess=random.randint(lowest,highest)+1
   if computer_guess>number_to_guess:
      highest=computer_guess
      computer_guess=random.randint(lowest,highest)-1
print"The number of times it took me was",attempts