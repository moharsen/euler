# Euler Project problem statement
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Answer: 
import math
def getprime(n):
    """
    Obtains the prime factors of number n

    Args:
    n - Natural number

    Returns:
    prime_factor - list of prime factors of n

    >>> getprime(24)
    [2, 3]

    >>> getprime(30)
    [2, 3, 5]

    >>> getprime(210)
    [2, 3, 5, 7]

    """
    prime_factor=[]

    # If n is even, reduce it to odd
    while n%2==0:
        prime_factor.append(2)
        n = n/2
        
    
    # Now, n is safely odd. calculating max divisor
    max_lim = int(max(math.sqrt(n),n+1))
    

    for divisor in range(3,max_lim+1,2):
        while n%divisor==0:
            prime_factor.append(divisor)
            n=n/divisor
    
    # Deduplicate
    prime_factor = list(set(prime_factor))

    return prime_factor

if __name__=='__main__':
    print(getprime(142))


    