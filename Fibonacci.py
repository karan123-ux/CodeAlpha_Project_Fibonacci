n = int(input("Enter the Number: "))

def fibonacci(n):
    fib_series = [0, 1]  # Initialize the series with the first two numbers
    
    # Generate Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]  # Calculate the next number
        fib_series.append(next_number)  # Add the next number to the series
    
    return fib_series

print("The Fibonacci series for ", n, "terms is:")
print(fibonacci(n))
