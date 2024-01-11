# three quotation marks are used to make a multiline string.

logo = """
_ _ _	 _				 _						 
| | | (_)	 | |			 | |						 
| |__| |_ __ _| |__ ___ _ __ | |	 _____	 _____ _ __ 
| __ | |/ _` | '_ \ / _ \ '__| | | / _ \ \ /\ / / _ \ '__|
| | | | | (_| | | | | __/ | | |___| (_) \ V V / __/ | 
|_| |_|_|\__, |_| |_|\___|_| |______\___/ \_/\_/ \___|_| 
			__/ |											 
		|___/											 
"""


vs = """
_ __ 
| | / /____
| | / / ___/
| |/ (__ ) 
|___/____(_)
"""


data = [
	{
		'name': 'Instagram',
		'follower_count': 346,
		'description': 'Social media platform',
		'country': 'United States'
	},
	{
		'name': 'Cristiano Ronaldo',
		'follower_count': 215,
		'description': 'Footballer',
		'country': 'Portugal'
	},
	{
		'name': 'Ariana Grande',
		'follower_count': 183,
		'description': 'Musician and actress',
		'country': 'United States'
	},
    {
		'name': 'Ariana',
		'follower_count': 156,
		'description': 'Musician and actress',
		'country': 'United States'
	}
]


# since we want to randomly select an 
# option from the data, we need random 
# module
import random
import os

# import the game data
data

import os

def clear_terminal():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Call the function to clear the terminal
clear_terminal()


def assign():
    return random.choice(data)
# Assuming p1 and p2 are dictionaries

def compare(p1,p2,user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']
    
    max = ''
    
    if sum1>sum2:
        max =p1['name']
    else:
        max =p2['name']
    
    if max == user_input:
        return True
    else:
        return False 
    

def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing= True
        while still_guessing:
            clear_terminal()
            print(logo)
            # assign 2 person names to display
            person1 = assign()
            person2 = assign()
            if person1==person2 and score ==0:
                    person2=assign()
                    person1=assign()
                    
            
            
            
            if score >0:
                person1 =person2
                person2=assign()
                
                if person1==person2:
                    person2=assign()
                    
            print(f"Name :{person1['name']},Desc:{person1['description']}")
            
            print(vs)
            
            print(f"Name :{person2['name']},Desc:{person2['description']}")
            
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")
            
            guess = input("Enter name of person with Higher Followers: ")
            
            if compare(person1, person2, guess):
               
                  # if user is correct continue to next iteration
                # and increase score by 1
                score += 1
            else:
                # if user is wrong, the current game play loop stops
                still_guessing = False
                
        play_again = input("Want to Play Again? (y/n): ").lower()
         
        # if he want to, continue, otherwise end the outer 
        # loop as well. also check if the user entered some
        # other input than what is allowed
        if play_again == 'y':
            clear_terminal()
            continue
        elif play_again == 'n':
            playing_game = False
            clear_terminal()
            print("Game Exited Successfully")
        else:
            playing_game = False
            print("Invalid Input Taken as no.")        
            
            
                   
                
            
            



want_to_play = input("Do you want to play Higher Lower?(Y/N)").lower()
if want_to_play=="y":
    clear_terminal()
    play_higher_lower()
elif want_to_play=='n':
    print("Program exit successfull")
else:
    print("Invalid input.Program exited")
    
    
    



    

    
    
