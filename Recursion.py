# Recursion is a process of using a function as a argument of the same function till the last output
'''Unlike iteration for values for one loop we use sometimes recursion untill the condition is satisfied'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))