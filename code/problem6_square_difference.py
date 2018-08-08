# Euler project problem statement
# The sum of the squares of the first ten natural numbers is,
#                           1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#                           (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Ans: 25164150

def square_difference(n):
    """
    Find the difference between 
    sum of squares of n natural numbers AND 
    the square of the sum

    Arg:
    n - A natural number

    Return:
    result - difference of between sum of squares of n natural numbers AND the square of the sum

    >>> square_difference(2)
    4.0

    >>> square_difference(3)
    22.0

    """

    return n*(n+1)*(3*n+2)*(n-1)/12

if __name__=='__main__':
    print(square_difference(100))

    