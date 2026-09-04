'''def number_of_even_numbers(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return n // 2
def number_of_odd_numbers(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return (n + 1) // 2
a = int(input("Enter a number: "))
even_count = number_of_even_numbers(a)
odd_count = number_of_odd_numbers(a)
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")'''


'''def sum_of_numbers(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return n * (n + 1) // 2
a = int(input("Enter a number: "))
total_sum = sum_of_numbers(a)
print(f"Sum of numbers from 1 to {a}: {total_sum}")'''


'''def sum_of_even_numbers(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    s=0
    for i in range(n + 1):
        if i % 2 == 0:
            s += i
    return s
a = int(input("Enter a number: "))
even_sum = sum_of_even_numbers(a)
print(f"Sum of even numbers from 1 to {a}: {even_sum}")'''


'''def factorial_of_number(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
a = int(input("Enter a number: "))
factorial_result = factorial_of_number(a)
print(f"Factorial of {a}: {factorial_result}")'''


'''def fibonacci_series(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    a, b = 0, 1
    for i in range(n):
        series = a
        a, b = b, a + b
        print(series)   
a = int(input("Enter a number: "))   
fibonacci_series(a)'''


'''def reverse_the_digits(n):
    if n < 0:
        n = -n
        n = str(n)[::-1]
        return -int(n)
    else:
        n = str(n)[::-1]
        return int(n)
a = int(input("Enter a number: "))
reversed_number = reverse_the_digits(a)
print("Reversed number: ", reversed_number)'''

'''def armstrong_number(n):
    for n in range(n + 1):
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        num_str = str(n)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        if sum_of_powers == n:
            print(n)
a = int(input("Enter a number until which to check Armstrong numbers: "))
armstrong_number(a)'''

'''def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    binary = "0 0 0 0 0 0 0 0"
    list_of_binary = binary.split(" ")
    index = 7
    while n > 0 and index >= 0:
        list_of_binary[index] = str(n % 2)
        n //= 2
        index -= 1
    return " ".join(list_of_binary)
a = int(input("Enter a number: "))
binary_representation = decimal_to_binary(a)
print("Binary representation: ", binary_representation)'''

'''def binary_to_decimal(binary_str):
    binary_str = binary_str.replace(" ", "")
    binary_list = list(binary_str)
    if len(binary_str) != 8 :
        raise ValueError("Input must be an 8-bit binary number.")
    value = 0
    for i in range(8):
        if int(binary_list[i]) % 2 == 0:
            value *= 2
        else:
            value = value * 2 + 1
    return value
a = input("Enter an 8-bit binary number (e.g., 00000000): ")
decimal_value = binary_to_decimal(a)
print("Decimal value: ", decimal_value)'''

'''def  number_of_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
a = int(input("Enter a number: "))
digit_count = number_of_digits(a)   
print("Number of digits: ", digit_count)'''