def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    if x == 0 or x == 1:
        return 1
    else:
        # calling function inside itself (recursion)
        return x * factorial(x - 1)

# display docstring
print(factorial.__doc__)
print("The factorial of 0:", factorial(0))     # 1
print("The factorial of 1:", factorial(1))     # 1
print("The factorial of 4:", factorial(4))     # 4 * 3 * 2 * 1 = 24
print("The factorial of 5:", factorial(5))     # 5 * 4 * 3 * 2 * 1 = 120
print("The factorial of 10:", factorial(10))   # 3628800
print("The factorial of 15:", factorial(15))
print("The factorial of 200:", factorial(200))
