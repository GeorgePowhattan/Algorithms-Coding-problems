'''You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.'''

# Solution:
import math

def staircase(x):
    nahoru = range((x // 2)+1, x+1)
    dolu = range((x // 2),-1,-1)
    suma = 0
    if  x % 2 == 1:
        for (n, k) in zip(nahoru, dolu):
            comb = (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
            suma = suma + comb
    else:
        for (n, k) in zip(range((x // 2), x+1), dolu):
            comb = (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
            suma = suma + comb
    
    return int(suma)

# Turns out the solution follows adjusted Fibonacci sequence (without the first 1).

def fib_staircase(x):
    
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return (fib_staircase(x-2) + fib_staircase(x-1))

# Example
print(staircase(5))
print(fib_staircase(5))
