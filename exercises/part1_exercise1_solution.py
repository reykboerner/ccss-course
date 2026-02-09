#Program prints the first 1000 primenumbers.
#Note that this is an example program and that there are many solutions possible.

#------------------------------------------------------------------------------
#-----------------------------------METHOD 1-----------------------------------
#------------------------------------------------------------------------------

counter = 1 
#Keeps track of the amount of prime numbers.
#Number 2 is the first one, therefore, counter = 1 (this way is much easier and faster!)
denominator = 2
number = 3
print("Number 2 is prime number 1")

while counter < 1000:
    #As long as the 1000th prime number is not reached,
    #we will continue our search...
    if number - 1 == denominator:
        #If you can not find any matches up to your potential candidate, 
        #you have found a prime number!
        print("Number", number, "is prime number", counter + 1)
        number = number + 2
        #Skip the even numbers
        counter = counter + 1
        #Add 1 to the prime counter
        denominator = 2
        #Set back the denominator and start over again.
    elif number % denominator == 0:
        #If you can devide your number, than your candidate is not a prime number.
        #Raise your potential candidate by 2 and reset your denominator and
        #start over again with a new number.
        number = number + 2
        denominator = 2
    else:
        denominator = denominator + 1
        #Raise the denominator each time by one if you did not find a
        #prime number or a non-prime number. 

#------------------------------------------------------------------------------
#-----------------------------------METHOD 2-----------------------------------
#------------------------------------------------------------------------------
print('\n\n\n')
counter = 0
#Keeps track of the amount of prime numbers.
number	= 2

while counter < 1000:
    #As long as the 1000th prime number is not reached,
    #we will continue our search...
    candidate	= True
    #Assume number is a prime number
    for denominator in range(2, number):
    	#Make for-loop for the denominator, ranging from 2 to number - 1
    	if number % denominator == 0:
    		#If you can devide your number, than your candidate is not a prime number.
    		#Set candidate to false and stop with the for-loop
    		candidate = False
    		break
    		
    if candidate:
    	#If True, you will pass the for-loop
    	counter += 1
    	print("Number", number, "is prime number", counter)
    			
    number += 1
    #Raise the number by 1
     
#------------------------------------------------------------------------------
#-----------------------------------METHOD 3-----------------------------------
#------------------------------------------------------------------------------

print('\n\n\n')

#Generate list to save all the prime numbers, include manually 2
prime_list	= [2]
number		= 3

while len(prime_list) < 1000:
    #As long as the 1000th prime number is not reached,
    #we will continue our search...
    candidate	= True
    #Assume number is a prime number
    
    for prime_i in prime_list:
    	#Take each element out of the prime list
    	#Divide each prime number of the list by the number (potential candidate)
    	
    	if number % prime_i	== 0:
    		#If you can devide your number by a prime, than your candidate is not a prime number.
    		#Set candidate to false and stop with the for-loop
    		candidate = False
    		break
    		
    if candidate:
    	#If True, you will pass the for-loop
    	prime_list.append(number)
    	print("Number", number, "is prime number", len(prime_list))
    			
    number += 2
    #Raise the number by 2 (skip even numbers)