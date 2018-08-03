# Project Euler Problem statement
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Min product: 100 x 100 = 10000
# Max product: 999 x 999 = 998001

def is_palindrome(input):
    """
    Check if palindrome

    Arg:
    Input - A text or number

    Return:
    True - If Input is palindrome
    False - Otherise

    >>> is_palindrome('Madam')
    False

    >>> is_palindrome('MADAM')
    True

    >>> is_palindrome(9009)
    True

    >>> is_palindrome(9098)
    False
    """
    
    return str(input)==str(input)[::-1]


def check_palindrome(d):
    """
    Obtain the greatest palindrome from the product of d digited integers

    Arg:
    d - An integer denoting the number of digits in the multiplicands

    Return:
    max_palindrome - The maximum palindrome obtained by product of 2 natural numbers with d-digits
    p1, p2 - The two natural numbers such that p1*p2 = max_palindrome

    >>> check_palindrome(2)
    (9009, 99, 91)

    
    """
    # Lower and upper bound of testing ranges
    ub = 10**d-1
    lb = 10**(d-1)

    # Initializing return parameters
    max_palindrome=0
    p1=ub
    p2=ub

    for i in range(ub,lb,-1):
        for j in range(ub,lb,-1):
            product = i*j
            if is_palindrome(product):
                if product>max_palindrome:
                    max_palindrome = product
                    p1=i
                    p2=j

    return max_palindrome, p1, p2
                
if __name__=='__main__':
    n,x,y = check_palindrome(3)
    print('{0} = {1} x {2}'.format(n,x,y))
    
    