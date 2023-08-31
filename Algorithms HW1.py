def foo_bar(n: int):
    for i in range(1, n + 1):
        # Check if the number is divisible by both 3 and 7 and print 'BinGo'
        if i % 3 == 0 and i % 7 == 0:
            print("BinGo")
        elif i % 3 == 0:
            print("Bin")
        elif i % 7 == 0:
            print("Go")
        else:
            print(i)


foo_bar(100)


def sum_numbers(n: int):
    # Initialize the variable 'final_sum' and set it to 0 initially
    final_sum = 0

    # Use a loop to iterate over numbers from 0 to n (inclusive)
    for i in range(n + 1):
        # Convert the current number 'i' to a string to access its digits
        num_str = str(i)

        # Iterate through the digits in the number string and add them to 'final_sum'
        for digit in num_str:
            final_sum += int(digit)

    # Return the 'final_sum' as the result
    return final_sum


n = 5
result = sum_numbers(n)
print(f"Result for n = {n}: {result}")


def find_max(a: int, b: int, c: int):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = 124
num2 = 21
num3 = 32
max_num = find_max(num1, num2, num3)
print(f"The maximum number is: {max_num}")


def leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False  # Not a leap year
        else:
            return True   # Leap year
    else:
        return False      # Not a leap year


year1 = 2020
year2 = 1900
year3 = 2000

print(f"Is {year1} a leap year? {leap_year(year1)}")
print(f"Is {year2} a leap year? {leap_year(year2)}")
print(f"Is {year3} a leap year? {leap_year(year3)}")


def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
        next_fib = fib_sequence[-1] + fib_sequence[-2]

        # Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(next_fib)

    return fib_sequence


n = 7
sequence = generate_fibonacci_sequence(n)
print(f"The Fibonacci sequence up to the {n}-th term is: {sequence}")
