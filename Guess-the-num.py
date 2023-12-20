import random
import math

lower = int(input("ENTER LOWER BOUND "))
upper = int(input("ENTER upper BOUND "))

x = random.randint(lower,upper)
print("\n\t You have only ",round(math.log(upper-lower + 1,2)),"chances to get the integer\n")

count = 0

while count < round(math.log(upper-lower + 1,2)):
    count+=1
    guess = int(input("Guess a number"))
    if x == guess:
        print("Congratulations you did it in ",count,"try")
        break
    elif x>guess:
        print("You guess too small")
    elif x<guess:
        print("You guess too high")
if count>round(math.log(upper-lower + 1,2)):
    print("\n The number is %d" %x)
    print("\t Better luck next time")
         
        


