# Python Program for Simple Interest'


#def simple_interest(p,t,r):
    #print("The principal is",p)
    #print("The time is",t)
    #print("The rate is",r)
    
    #si = (p*t*r)/100
    
    
    #print("The simple interest is", si)
    
    #return si


#simple_interest(10,4,5)


# Python3 program to find simple interest
#  principal amount, time and
# rate of interest taken from user.

def si(p,t,r):
    print("The principal is",p)
    print(f'The rate os interest is {r}')
    print("The time is ",t)
    
    
    si = (p*t*r)/100
    
    print("The simple interest is ",si)
    
    return si

pr = int(input("Enter the principal"))
rate = int(input("Enter the rate"))
time = int(input("Enter the time"))

si(pr,rate,time)


