
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "invalid name"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "invalid number"
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    player_choice = input("Choose: rock, paper, scissors, lizard, or Spock: ")

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randint(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "You chose", player_choice
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    num = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    
    # if the difference is 1 or 2, computer wins
    if (num == 1) or (num == 2):
        print "Computer wins!"
        
    # otherwise, if the difference is 3 or 4, the player wins
    elif (num == 3) or (num == 4):
        print "Player wins!"
        
    # if computer and player chose the same, the result is a tie
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

