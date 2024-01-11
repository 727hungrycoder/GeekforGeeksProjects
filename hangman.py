import random
words = ["apple","banana","mango"]
random_word= random.choice(words)

print("Guess the characters")
#print(random_word)

guessed_word = ""
 
 
turns = len(random_word) + 2
# print(turns)

while turns>0:
    failed = 0
    for ch in random_word:
        if ch in guessed_word:
            print(ch,end="")
        else:
            print("_",end="")
            failed+=1
    if failed == 0:
        print(f"You guessed the correct word {random_word}")
        print("You Win")
        break
        

    print()
    
    guess = input("Please enter the correct guess")
    guessed_word+=guess

    if guess not in random_word:
            turns-=1
            print(f"you have {turns} turns left.Please try again")
            if turns==0:
                print("You loose.")
            
        
        
        
            
            
            
            
