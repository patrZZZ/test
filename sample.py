# Python program to display all the prime numbers within an interval*****************************************************

# change the values of lower and upper for a different result
lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
*****************************************************           
# Initialize a list
primes = []
for possiblePrime in range(2, 21):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break 
    if isPrime:
        primes.append(possiblePrime)           
        
 *****************************************************       
import time 
def SieveOfEratosthenes(n): 
       
    # Create a boolean array "prime[0..n]" and  
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
      
    p = 2
    while(p * p <= n): 
           
        # If prime[p] is not changed, then it is  
       # a prime 
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    c = 0
  
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            c += 1
    return c  
# Driver function 
t0 = time.time() 
c = SieveOfEratosthenes(100000) 
print("Total prime numbers in range:", c) 
  
t1 = time.time() 
print("Time required:", t1 - t0) 


#*****************************************************
Recursive function

import sys
sys.setrecursionlimit(3000)
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)



