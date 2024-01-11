# Python Program to Find the Factorial of a Number


#def factorial(n):
#    return 1 if (n==1 or n==0) else n*factorial(n-1)



#num =5
#print(factorial(num))



# Find the Factorial of a Number Using Iterative approach

#def factorial(n):
#    if n<0:
#        return 0
 #   elif n==0 or n==1:
#        return 1
#    else:
 #       fact = 1
#        while(n>1):
#            fact *= n
#            n-=1
#        return fact
        
        
        
#num = 5

#print(factorial(num))


# Python 3 program to find
# factorial of given number
  
# Function to find factorial of given number

#def factorial(n):
    #res = 1
    
    
#    for i in range(2,n+1):
#        res*=i
#    return res

#num = 5
#print(factorial(num))
            
            
# Find the Factorial of a Number Using One line Solution (Using Ternary operator): 

#def factorial(n):
#    return 1 if (n==1 or n==0) else n * factorial(n-1) 

#num = 5

#print(factorial(num))

# Find the Factorial of a Number Using using In-built function 

#import math
#def factorial(n):
 #   return(math.factorial(n))

#num =5

#print(factorial(num))


# Find the Factorial of a Number Using numpy.prod 

#import numpy

#n =5

#x = numpy.prod([i for i in range(1,n+1)])

#print(x)
       
       
# Prime Factorization Method to find Factorial

# Function to find prime factors of a number

#def primefactors(n):
#    factors ={}
#    i =2
#    while i*i <= n:
#        while n%i ==0:
#            if i not in factors:
#                factors[i]=0
#            factors[i]+=1
#            n//=i
#        i+=1
        
#    if n>1:
#        if n not in factors:
#            factors[n]=0
#            factors[n]+=1
#    return factors



# Function to find factorial of a number

# The Fundamental Theorem of Arithmetic states that every natural number greater than 1 can be written as a product of prime numbers , and that up to rearrangement of the factors, this product is unique . This is called the prime factorization of the number.

#def factorial(n):
 #   result = 1
#    for i in range(2,n+1):
#        factors=primefactors(i)
 #       for p in factors:
#            result*=p ** factors[p]
#    return result
#        
                
        
#print(factorial(5))       
    
    


       


            
            

        
    


