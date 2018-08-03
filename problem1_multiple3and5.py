# Euler Project Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 2318



def get_multiples_nxy(n, x, y):
    """
    This obtains the list of natural numbers below n that are multiples of x and y

    Args:
    n - The maximum natural number
    x - Natural number less than n
    y - Natural number less than n


    Returns:
    multiples - List of natural numbers less than n that are multiples of x and y

    
    >>> get_multiples_nxy(10, 3, 5)
    [3, 5, 6, 9]

    >>> get_multiples_nxy(15, 5, 7)
    [5, 7, 10, 14]
    """
    multiples = [i for i in range(1,n) if (i%x==0 or i%y==0)]
    return multiples

if __name__=='__main__':
    print(sum(get_multiples_nxy(100,3,5)))




