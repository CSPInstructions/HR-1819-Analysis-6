# We define a function that calculates the factorial of a number
def fac( number ):
    # We check whether we are dealing with an integer and whether that integer is greater then 0
    if not isinstance( number, int ) or number < 1:
        # If the conditions aren't met, we raise an error
        raise ValueError
    
    # We create a result variable that will be used to accumulate the result
    result = 1

    # We start looping, decreasing the value of number as we go, 
    # multiplying the value of result with the current number
    while number > 0:
        # Multiply the current result with the current number
        result = result * number

        # We decrease the number by 1
        number = number - 1

    # We return the final result
    return result