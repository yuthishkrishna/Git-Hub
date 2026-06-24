def square_root_bisection(number, tolerance=0.01, iteration=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number in [0, 1]:
        print(f'The square root of {number} is {number}')
        return number
    else:
        # For all other positive numbers, use bisection method
        a, b = 0, max(1, number)
        mid = 0
        for i in range(iteration):
            mid = (a + b) / 2
            mid_squared = mid ** 2
            
            # Check if interval is small enough or if mid^2 is within tolerance of target
            # Adjust the tolerance check to account for the relationship between mid error and mid^2 error
            if abs(mid_squared - number) < tolerance * mid:
                print(f"The square root of {number} is approximately {mid}")
                return mid
            
            if mid_squared > number:
                b = mid
            else:
                a = mid
        
        # If loop completes without converging
        print(f"Failed to converge within {iteration} iterations")
        return None
