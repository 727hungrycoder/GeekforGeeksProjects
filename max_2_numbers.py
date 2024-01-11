#def maximum(a,b):
#    if a>=b :
#        print(a)
#    else:
#        print(b)
        
        
        
#maximum(10,15)


# Python program to find the
# maximum of two numbers using max function

#a=2
#b=4

#c=max(a,b)

#print(c)



# Maximum of two numbers Using lambda function 

#a= 2
#b=4

#maximum = lambda a,b: a if a>b else b
#print(maximum(a,b))


# Maximum of two numbers Using list comprehension

#a =2 
#b=4

#x = a if a>b else b

#print("maximum number is",x)


# Maximum of two numbers Using sort() method


#a = 2
#b= 4

#x = [a,b]

#x.sort()

#print(x[-1])

# Python Program to Find the Factorial of a Number


#def factorial(n):
#    return 1 if (n==1 or n==0) else n*factorial(n-1)



#num =5
#print(factorial(num))



# Find the Factorial of a Number Using Iterative approach

def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact =1
        while(n>1):
            fact *= n
            n-=1
            return fact
        
        
        
num = 5

print(factorial(num))
            
        
    


