# Step 1: Define test case functions
def test_case_1():
    # Checking if 2 + 2 equals 4
    return 2 + 2 == 4

def test_case_2():
    # Check if length of "hello" is 5
    return len("hello") == 5

def test_case_3():
    # Check if 10 is greater than 20
    return 10 > 20

def test_case_4():
    # Check if "Python".upper() gives "PYTHON"
    return "Python".upper() == "PYTHON"

# Store all test cases in a list
test_cases = [test_case_1, test_case_2, test_case_3, test_case_4]

# Step 3: Execute test cases one by one and print summary
print("Mini Test Case Executor Results")

for i, test in enumerate(test_cases, start=1):
    result = test()  # Run the test case
    status = "PASS" if result else "FAIL" # printing true or false
    print(f"Test Case {i}: {status}")

print("Execution Completed")