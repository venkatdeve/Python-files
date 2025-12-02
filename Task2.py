# Function to calculate factorial of a number
def factorial(n):
    # Factorial is not defined for negative numbers
    if n < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        fact *= i
    return fact


# Function to return the nth Fibonacci number
def fibo(n):
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    # Start with first two Fibonacci numbers
    fir, sec = 0, 1
    for i in range(2, n):
        fibosum = fir + sec
        fir = sec
        sec = fibosum
    return sec


# Function to check if a number is prime
def is_prime(n):

    for i in range(2 , n):
        if n % i == 0:
            return False
    else:
        return True


# Function to calculate sum of elements in a list
def sum_of_list(list1):
    total = 0
    for i in list1:
        total += i
    return total


# ---------------- DEMO ----------------
print("Factorial of 5:", factorial(5))       # 120
print("8th Fibonacci number:", fibo(8))      # 13
print("Is 9 prime?", is_prime(9))            # False
print("Sum of list:", sum_of_list([1,2,3,4,5]))  # 15