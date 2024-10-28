def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...

    output = True

    for check in range(2, num+1):

        if num % check == 0 and num != check: # if its divisible by any number that isnt itself it is False
            output = False
            break

    return output

# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
