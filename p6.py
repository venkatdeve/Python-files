def add(a, b):
    # Returns the sum of two numbers a and b.
    return a + b

def subtract(a, b):
    # Returns the result of subtracting b from a.
    return a - b

def is_even(n):
    # Returns True if the number n is even, otherwise False.
    return n % 2 == 0

# Test cases with pass/fail output
def run_tests():
    try:

        assert add(3, 4) == 7
        print("add test 1 passed")
    except AssertionError:
        print("add test 1 failed")

    try:
        assert add(-2, 5) == 3
        print("add test 2 passed")
    except AssertionError:
        print("add test 2 failed")

    try:
        assert subtract(10, 3) == 7
        print("subtract test 1 passed")
    except AssertionError:
        print("subtract test 1 failed")

    try:
        assert subtract(5, 10) == -5
        print("subtract test 2 passed")
    except AssertionError:
        print("subtract test 2 failed")

    try:
        assert is_even(6) == True
        print("is_even test 1 passed")
    except AssertionError:
        print("is_even test 1 failed")

    try:
        assert is_even(7) == False
        print("is_even test 2 passed")
    except AssertionError:
        print("is_even test 2 failed")

run_tests()