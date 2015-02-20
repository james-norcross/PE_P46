## Author: James Norcross
## Date: 2/20/15
## Description: finds first odd composite number that cannot be
## expressed as the sum of a prime and 2 times a square

from math import sqrt

## a prime sieve function
def makePrimeSieve(max):
    sieve = []
    
    ## initialize to true
    for i in range(max):
        sieve.append(True)
        
    ## make sieve
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True
    
    imax = int(sqrt(max)) + 1
    
    for i in range(2,imax):
        if(sieve[i]):
            for j in range(2*i, max, i):
                sieve[j] = False

    return sieve

max = 1000000
sieve = makePrimeSieve(max)

done = False

## step through odd composites C
i = 9
while(i < max and not done):
    if(not sieve[i] and i%2 != 0):
        ## loop through possible values of 2*j^2
        j = 1
        while(True):
            ## if reach end of possible range of 2*j^2 then have found answer
            if(i - 2*j*j < 0):
                done = True
                print str(i) + " is the answer"
                break
            ## if difference C - 2*j^2 is prime move to next C
            elif(sieve[i - 2*j*j]):
                break
            ## consider next j
            else:
                j += 1
    i += 1
print "done"
        
    
