import random
num = random.randrange(1000,10000)

n = int(input("Guess the 4 digit number"))

if n==num:
    print("Great!You are a Mastermind.You guessed the number in just 1 try.")


else:
    ctr= 0
    
    while(n!=num):
        ctr+=1
        count =0
        n = str(n)
        num=str(num)
        
        correct = ["X"] * 4
        
        for i in range(0,4):
            if n[i] == num[i]:
                count+=1
                correct[i]=n[i]
            else:
                continue
            
            print("Not quite the number. But you did get ",
                  count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=' ')  
            print('\n')
            print('\n')    
            1
            n = int(input("Enter your next choice of numbers: "))
            n= str(n)
            
        if n == num:
            # ctr must be incremented when the n==num gets executed as we have the other incrmentation in the n!=num condition
            ctr += 1
            print("You've become a Mastermind!")
            print("It took you only", ctr, "tries.")
        # when none of the digits are guessed correctly.
        elif count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))         