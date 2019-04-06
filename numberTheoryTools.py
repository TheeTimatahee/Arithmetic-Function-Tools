import math

def isDivisible(a,b):
    """Checks if a is divisble by b, true if yes, false otherwise"""
    return (a%b) == 0

def positiveFactors(n):
    """Returns a list of all the positive prime factors of n"""
    positiveFactors = []
    n = int(n) #assert n is int
    #Loops through all integers in range [0,n]
    for x in range(1,(n+1)):
        #Checks if n is divisible by x
        if(isDivisible(n,x)):
            #If it is add it to the list of factors
            positiveFactors.append(x)
    return positiveFactors

def primeNumbers(n):
    """Sieve of Eratosthenes"""
    p = []
    #"Sand" is all the integers in the range [2,n]
    sand = list(range(2,(n+1)))
    #While theres still integers left to check, keep looping
    while(len(sand) != 0):
        #Get the first element of the list;
        #divisor should be prime
        divisor = sand[0]
        #Loop through all remaining integers in range
        for num in sand:
            #Check if num is divisble by the first element
            if(isDivisible(num,divisor)):
                #If it is, remove it from the list of integers
                sand.remove(num)
        #Add the prime to the list then continue
        p.append(divisor)
    return p

def isPrime(n):
    """Determines if n is prime via brute-force"""
    #1 isn't prime, so eliminate this case
    if(n==1):
        return False
    #Loops through all integers in range [0,(n-1)]
    for x in range(2,n):
        #Checks if n is divisible by the current element
        if(isDivisible(n,x)):
            #If it is, n is not prime therefore return False
            return False
    # n is prime if it survives all previous cases, 
    # ie if n isn't divisble by any number in the range [0,(n-1)]
    return True

def checkFactorization(factorization,n):
    """Checks if n is part of the current factorization, if it isn't, checkFactorization adds it to the set"""
    for (p,a) in factorization:
        # Checks if the current factor's base is equal to n
        if(p==n):
            # If it is, remove that element from the set,
            # then add a new one with it's exponent incremented
            # and return the updated factorization
            factorization.remove((p,a))
            factorization.add((p,(a+1)))
            return factorization
    # If it reaches this point, n is not in the factorization,
    # so add it with an exponent of 1, then return the update factorization
    factorization.add((n,1))
    return factorization

def primeFactorization(n):
    """Returns the prime factorization of n in the form of a set of ordered pairs, 
    where the first element is the base and the second is the exponent"""
    factorization = set({})
    # Gets all the prime numbers within [2,n]
    primes = primeNumbers(n)
    i = 0
    # As long as theres still factors to extract, continue
    while(n > 1):
        # Get the next prime number to extract
        p = primes[i]
        # As long as p can be factored out of n, remove it then add it to factorization
        while(isDivisible(n,p)):
            # Add p to the factorization if it hasn't already been,
            # or increment it's exponent by 1
            factorization = checkFactorization(factorization,p)
            # Remove one p term from n
            n /= p
        # Increment the index by 1 to get the next prime to check
        i += 1
    return factorization

def tau(n):
    """Returns the number of positive factors of n"""
    return len(positiveFactors(n))

def sigma(n):
    """Returns the sum of the positive factors of n"""
    return sum(positiveFactors(n))

def one(n):
    """1 function: simply returns 1, regardless of input"""
    return 1

def iden(n):
    """Identity function: returns n"""
    return n

def littleOmega(n):
    """little Omega function: returns the number of distinct prime factors of n"""
    omega = 0
    # Loops through all the positive factors of n
    for x in positiveFactors(n):
        # Checks if the current factor is prime
        if(isPrime(x)):
            # If it is, increment omega by 1
            omega += 1
    return omega

def BigOmega(n):
    """Big Omega function: returns the sum of
     all the exponents in the prime factorization of n"""
    factorization = primeFactorization(n)
    sum = 0
    for (p,a) in factorization:
        sum += a
    return sum

def phi(n):
    """Returns the number of integers <= n, such that
    they are relatively prime with n"""
    num = 0
    # Loops through all integers [1,n]
    for x in range(1,(n+1)):
        # Checks if x is relatively prime with n
        if(math.gcd(x,n) == 1):
            # Increments num if it is
            num += 1
    return num

def phiAlt(n):
    """Returns the *sum* of integers <= n, such that
    they are relatively prime with n"""
    sum = 0
    # Loops through all integers [1,n]
    for x in range(1,(n+1)):
        # Checks if x is relatively prime with n
        if(math.gcd(x,n) == 1):
            # Adds x to the sum if it is
            sum += x
    return sum

def flambda(n):
    """Von Mangoldt Function"""
    factorization = primeFactorization(n)
    # If the prime factorization of n is just one term, return log n
    if(len(factorization) == 1):
        return math.log(n)
    # Otherwise return 0
    else: 
        return 0

def mu(n):
    """Mobius mu-function"""
    # If n is 1, return 1
    if(n==1):
        return 1
    factorization = primeFactorization(n)
    # Loop through all the terms of the prime factorization of n
    for (p,a) in factorization:
        # If any terms have exponents >= 2, then return 0
        if(a>=2):
            return 0
    # Any n's that reach this point have prime factorizations with all terms having
    # exponents of 1. Return (-1)^(number of terms)
    return (-1)**(len(factorization))

def dirichletProduct(f,g,n):
    """Also know as Dirichlet convolution"""
    sum = 0
    # Loops through all integers in range [1,n]
    for d in range(1,(n+1)):
        # Checks if the current integer divides n
        if(isDivisible(n,d)):
            # If it does, add the multiplication of f(d)*g(n/d) to the overall sum
            sum += f(d) * g(n/d)
    return sum

def e(n):
    """Identity function for dirichlet convolutions, ie 
    dirichletProduct(f,e,n) = f(n), for some arithmetic function f"""
    if(n==1):
        return 1
    else:
        return 0

def inverseF(f,n):
    return mu(n)*f(n)