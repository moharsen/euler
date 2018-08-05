# Euler project problem statement
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Logic: To find LCM between x and y, preseve x=x', add x' to the remainder of x/y till the remainder vanishes
# Ans: 232792560

def smallest_multiple(n):
    """
    Return the number that evenly divides the first n natural numbers
    Implemented as per the solution provided in StockOverflow
    https://stackoverflow.com/a/31736020

    Arg:
    n - A natural number

    Return:
    result - The smallest number that evenly divides the first n natural numbers

    >>> smallest_multiple(10)
    2520

    >>> smallest_multiple(11)
    27720

    """
    result = 1
    prev=None
    for i in range(1,n+1):
        prev = result
        # print('\ninitial i = {0}, prev={1} , result = {2}'.format(i,prev,result)) # explanatory print
        while (result%i > 0):
            print('result%i = {0}'.format(result%i))
            result += prev
        #     print('result = result+prev = {0}'.format(result)) # explanatory print
        # print('final i = {0}, prev={1} , result = {2}'.format(i,prev,result)) # explanatory print
    return result

if __name__=='__main__':
    print(smallest_multiple(3))
       
   