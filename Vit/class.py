def sum(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return n*(n+1)//2
b = input("Enter a number: ")
if isinstance(b, int):
    b = int(b)
    a = sum(b)
    print(a)
else:
    print("Please enter a valid integer.")